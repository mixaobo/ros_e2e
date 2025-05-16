#!/usr/bin/env python2
import rospy
import numpy as np
from ros_basics_turorials.msg import Localize
from scipy.optimize import least_squares



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


def wrap_angle(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi

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
        y[1] = wrap_angle(y[1])

        S = H.dot(self.P).dot(H.T) + self.R
        K = self.P.dot(H.T).dot(np.linalg.inv(S))
        self.x = self.x + K.dot(y)
        self.P = (np.eye(2) - K.dot(H)).dot(self.P)

    def current_position(self):
        return self.x

def chatter_callback(msg):
    global pub_server
    
    d = msg.Distance
    aoa_rad = np.deg2rad(msg.AoA)
    z = np.array([d, aoa_rad])
    ekf.predict()
    ekf.update(z, anchor1)
    
    #Debug msg
    received_xy = calculate_initial_guess(anchor1, msg.Distance, msg.AoA)
    print("Received Position x/y: ", received_xy)
    predict_xy = ekf.current_position()
    deviation = np.abs((np.linalg.norm(predict_xy) - np.linalg.norm(received_xy)))
    if (deviation >= 5):
        print("Deviation too large, ignoring prediction")
    else:
        #public position to other node
        print("EKF Position x/y:", predict_xy)
        ranging_msg = Localize()
        predict_distance, predict_angle = calcualte_distance_angle(0, 0, predict_xy[0], predict_xy[1])
        ranging_msg.Distance = predict_distance
        ranging_msg.AoA = predict_angle
        pub_server.publish(ranging_msg)
    print("------------")

def Node_localize():
    global pub_server
    #Initialize
    rospy.init_node('node_localize', anonymous=True)

    #Publish to node_server
    pub_server = rospy.Publisher('topic_localize', Localize, queue_size=10) 

    # subscribe to node_ethernet
    rospy.Subscriber('chatter', Localize, chatter_callback)
    rospy.spin()

# Initial state
# P:  < 1: trust more on inital predictions / ~5: balance / >10: trust more on measurements
# Q: 0.01: standstill/ 0.1: Slow movement / fast movement 0.3 ~ 0.5 / Vehicle: 1.0+
# R Small: trust measurrements / Large: trust predictions. variance = standard_deviation**2
initial_x = calculate_initial_guess(anchor1, 60, 40)
ekf = ExtendedKalmanFilter(
    x_init=initial_x,
    P_init=np.eye(2) * 5,
    Q=np.eye(2) * 0.3,
    R=np.diag([1.0, np.deg2rad(1.0)**2]) 
)

if __name__ == '__main__':
    Node_localize()
