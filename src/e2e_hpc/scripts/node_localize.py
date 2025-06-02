#!/usr/bin/env python2
import rospy
import threading
import numpy as np
from e2e_hpc.msg import CustomMsg_Ranging




"""
#This function calculates the residuals for the optimization problem.
def residuals(p, anchor, d, aoa_rad):
    x, y = p
    dx, dy = x - anchor[0], y - anchor[1]
    pred_d = np.hypot(dx, dy)
    pred_aoa = np.arctan2(dy, dx)
    return [pred_d - d, wrap_angle(pred_aoa - aoa_rad)]



def estimate_position(d, aoa_deg):
    aoa_rad = np.deg2rad(aoa_deg)
    initial_guess = calculate_initial_guess(anchor1, d, aoa_deg)
    result = least_squares(residuals, initial_guess, args=(anchor1, d, aoa_rad), method='lm')
    return result.x
"""
anchor1 = np.array([0.0, 0.0])  # Fixed anchor position
Sync_Flag = [0,0]
RangingMsg_Passenger = CustomMsg_Ranging()
RangingMsg_Driver = CustomMsg_Ranging()
RangingMsg_Passenger_Event = threading.Event()
RangingMsg_Driver_Event = threading.Event()
threading_lock = threading.Lock()
previous_aoa = 0.0


def wrap_angle_radians(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi

def wrap_angle_360(angle):
    """Wrap angle to [0, 360) degrees."""
    return angle % 360

def calculate_initial_guess(anchor, d, aoa_deg):
    aoa_rad = np.deg2rad(aoa_deg)
    x = anchor[0] + d * np.cos(aoa_rad)
    y = anchor[1] + d * np.sin(aoa_rad)
    return np.array([x, y])

def calcualte_distance_angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = np.hypot(dx, dy)
    angle_rad = np.arctan2(dy, dx)
    angle_deg = np.rad2deg(angle_rad)
    return distance, angle_deg

class ExtendedKalmanFilter:
    def __init__(self, x_init, P_init, Q, R):
        self.x = x_init
        self.P = P_init
        self.Q = Q
        self.R = R

    def predict(self):
        self.P = self.P + self.Q

    def update(self, z, anchor):
        px, py = self.x
        dx, dy = px - anchor[0], py - anchor[1]
        d_pred = np.hypot(dx, dy)
        aoa_pred = np.arctan2(dy, dx)
        z_pred = np.array([d_pred, aoa_pred])

        r2 = dx**2 + dy**2
        H = np.array([
            [dx/d_pred, dy/d_pred],
            [-dy/r2,     dx/r2]
        ])

        y = z - z_pred
        y[1] = wrap_angle_radians(y[1])

        S = H.dot(self.P).dot(H.T) + self.R
        K = self.P.dot(H.T).dot(np.linalg.inv(S))
        self.x = self.x + K.dot(y)
        self.P = (np.eye(2) - K.dot(H)).dot(self.P)

    def current_position(self):
        return self.x

class ExtendedKalmanFilterPolar:
    def __init__(self, x_init, P_init, Q, R):
        self.x = x_init  # [distance, aoa_rad]
        self.P = P_init
        self.Q = Q
        self.R = R

    def predict(self):
        # For static or simple motion, prediction may be identity
        self.P = self.P + self.Q

    def update(self, z):
        # z = [measured_distance, measured_aoa_rad]
        y = z - self.x
        y[1] = wrap_angle_radians(y[1])  # Ensure angle difference is wrapped

        H = np.eye(2)  # Measurement matrix is identity
        S = np.dot(np.dot(H, self.P), H.T) + self.R
        K = np.dot(np.dot(self.P, H.T), np.linalg.inv(S))
        self.x = self.x + np.dot(K, y)
        self.x[1] = wrap_angle_radians(self.x[1])  # Keep angle in [-pi, pi]
        self.P = np.dot((np.eye(2) - np.dot(K, H)), self.P)

    def current_position(self):
        # Returns distance and AoA in degrees
        return self.x[0], np.rad2deg(self.x[1])

def Ranging_callback(ekf_class, msg, publish_to_node):
    d = msg.distance
    aoa_rad = np.deg2rad(msg.aoa)
    z = np.array([d, aoa_rad])
    ekf_class.predict()
    ekf_class.update(z)
    
    #Debug msg
    received_xy = calculate_initial_guess(anchor1, msg.distance, msg.aoa)
    print("Kalman input  {} / {}".format(msg.distance, msg.aoa))
    predict_distance, predict_angle = ekf_class.current_position()
    
    #predict_distance, predict_angle = calcualte_distance_angle(0, 0, predict_xy[0], predict_xy[1])
    print("Kalman output {} / {}".format(predict_distance, predict_angle))
    msg_localization = CustomMsg_Ranging()
    msg_localization = msg
    msg_localization.distance = predict_distance
    msg_localization.aoa = predict_angle
    #previous_aoa = predict_angle
    publish_to_node.publish(msg_localization)  
    print("------------")    

    
def Ranging_Passenger_callback(msg):
    global RangingMsg_Passenger
    with threading_lock:
        RangingMsg_Passenger = msg
        #RangingMsg_Passenger.system_time = msg.header.stamp
    RangingMsg_Passenger_Event.set()

counter = 0
current_aoa = 0.0
def Ranging_Driver_callback(msg):
    global RangingMsg_Driver, counter, current_aoa, previous_aoa
    print("Anchor received value  {} / {}".format(msg.distance, msg.aoa))
    current_aoa = msg.aoa
    if (counter >= 10):
        if(counter == 10):
            previous_aoa = current_aoa
        counter = 11
        # if (previous_aoa >= 50):
        #     if (-70 <= current_aoa <= -50):
        #         current_aoa = previous_aoa

        if (np.abs(previous_aoa - current_aoa) > 60):
            msg.aoa = previous_aoa
            
        else:
            previous_aoa = current_aoa
            
        with threading_lock:
            RangingMsg_Driver = msg
            #RangingMsg_Driver.system_time = msg.header.stamp
        RangingMsg_Driver_Event.set()
        
    counter += 1

def background_thread():
    global ekf_driver, ekf_passenger, pub_Localization_Driver, pub_Localization_Passenger, RangingMsg_Driver, RangingMsg_Passenger

    while not rospy.is_shutdown():
        if(RangingMsg_Driver_Event.wait(timeout=0.01) == True):
            with threading_lock:
                Ranging_callback(ekf_driver, RangingMsg_Driver, pub_Localization_Driver)
                RangingMsg_Driver_Event.clear()
        if(RangingMsg_Passenger_Event.wait(timeout=0.01) == True):
            with threading_lock:    
                Ranging_callback(ekf_passenger, RangingMsg_Passenger, pub_Localization_Passenger)
                RangingMsg_Passenger_Event.clear()
        if rospy.is_shutdown():
            break
        
            
        
        

def Node_Ranging():
    global pub_Localization_Driver, pub_Localization_Passenger
    #Initialize
    rospy.init_node('node_Ranging', anonymous=True)

    #Publish to
    pub_Localization_Driver = rospy.Publisher('topic_Localization_Driver', CustomMsg_Ranging, queue_size=10)
    pub_Localization_Passenger = rospy.Publisher('pub_Localization_Passenger', CustomMsg_Ranging, queue_size=10)

    #Subscribe to
    rospy.Subscriber('topic_Ranging_Driver', CustomMsg_Ranging, Ranging_Driver_callback)
    rospy.Subscriber('topic_Ranging_Passenger', CustomMsg_Ranging, Ranging_Passenger_callback)

    # Start a background thread to keep the node alive
    bg_thread = threading.Thread(target=background_thread)
    bg_thread.daemon = True
    bg_thread.start()
    print("Start node")
    rospy.spin()


# Initial state
# P:  < 1: trust more on inital predictions / ~5: balance / >10: trust more on measurements
# Q: 0.01: standstill/ 0.1: Slow movement / fast movement 0.3 ~ 0.5 / Vehicle: 1.0+
# R Small: trust measurrements / Large: trust predictions. variance = standard_deviation**2
initial_x = calculate_initial_guess(anchor1, 10, 40)
ekf_driver = ExtendedKalmanFilterPolar(
    x_init=[10.0, 40.0],  # Initial position guess (x, y)
    P_init=np.eye(2) * 100,
    Q=np.eye(2) * 5.0,
    R=np.diag([5**2, np.deg2rad(3.0)**2]) #(cm, aoa)
)

ekf_passenger = ExtendedKalmanFilterPolar(
    x_init=[10.0, 40.0],
    P_init=np.eye(2) * 100,
    Q=np.eye(2) * 5.0,
    R=np.diag([5**2, np.deg2rad(3.0)**2]) #(cm, aoa)
)

if __name__ == '__main__':
    Node_Ranging()
