#!/usr/bin/env python2
import rospy
import numpy as np
from ros_basics_turorials.msg import Localize
from scipy.optimize import least_squares

anchor1 = np.array([0, 0])

# Residual function for optimization
def residuals(p, anchor1, d1, aoa1):
    x, y = p  # Estimated position (x, y)
    
    # Distance residuals
    r1 = np.linalg.norm([x - anchor1[0], y - anchor1[1]]) - d1
    
    # Angle residuals
    a1 = np.arctan2(y - anchor1[1], x - anchor1[0]) - np.deg2rad(aoa1)
    
    return [r1, a1]

# Estimate position using least squares 
def estimate_position(d1, aoa1):
    global anchor1
    initial_guess = calculate_coordinates(anchor1, 60.0, 40.0)
    result = least_squares(residuals, 
                        initial_guess,
                        args=(anchor1, d1, aoa1),
                        method='lm')
    return result.x

def calculate_coordinates(anchor1, d1, aoa1):
    """
    Calculate the coordinates of the object using trilateration.
    """
    # Convert angles from degrees to radians
    aoa1_rad = np.deg2rad(aoa1)

    # Calculate the coordinates
    x = anchor1[0] + d1 * np.cos(aoa1_rad)
    y = anchor1[1] + d1 * np.sin(aoa1_rad)

    # Return the coordinates as a NumPy array
    coordinates = np.array([x, y])
    return coordinates

self_x = calculate_coordinates(anchor1, 60.0, 40.0)  # Initial state closer to the expected position
self_P = np.eye(2) * 5  # Reduced initial uncertainty
self_Q = np.eye(2) * 0.5  # Smaller process noise
self_R = np.diag([10, np.deg2rad(8)**2])  # base on spec or real test

class ExtendedKalmanFilter:
    global self_x, self_P, self_Q, self_R
    def __init__(self):
        self.x = self_x
        self.P = self_P
        self.Q = self_Q
        self.R = self_R
    
    def predict(self):
        # Prediction step (no motion model, so state remains the same)
        self.P = self.P + self.Q

    def update(self, z, anchor1):
        # Measurement model
        px, py = self.x
        d1_pred = np.sqrt((px - anchor1[0])**2 + (py - anchor1[1])**2)
        aoa1_pred = np.arctan2(py - anchor1[1], px - anchor1[0])
        z_pred = np.array([d1_pred, aoa1_pred])

        # Jacobian of the measurement model
        d1_dx = (px - anchor1[0]) / d1_pred
        d1_dy = (py - anchor1[1]) / d1_pred
        dx = px - anchor1[0]
        dy = py - anchor1[1]
        r2 = dx**2 + dy**2

        aoa1_dx = -dy / r2
        aoa1_dy = dx / r2
        H = np.array([[d1_dx, d1_dy],
                      [aoa1_dx, aoa1_dy]])

        # Update step
        y = z - z_pred  # Measurement residual
        y[1] = (y[1] + np.pi) % (2 * np.pi) - np.pi
        S = np.dot(np.dot(H, self.P), H.T) + self.R  # Residual covariance
        K = np.dot(np.dot(self.P, H.T), np.linalg.inv(S))  # Kalman gain
        self.x = self.x + np.dot(K, y)  # Update state estimate
        self.P = np.dot((np.eye(2) - np.dot(K, H)), self.P)  # Update covariance

    def current_position(self):
        return self.x
    
def chatter_callback(msg):
    # Logs the message received on the 'chatter' topic along with the caller ID of the node.
    global ekf
    parsedata = Localize()
    parsedata.AoA = msg.AoA
    parsedata.Distance = msg.Distance
    print(parsedata)
    ekf.predict()
    ekf.update(np.array([parsedata.Distance, parsedata.AoA]), anchor1)
    print(ekf.current_position())
    print("--------")
    

def listener():
    # Initializes a ROS node named 'listener'. The `anonymous=True` argument ensures that
    # if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('listener', anonymous=True)
    
    # Subscribes to the 'chatter' topic, which uses the `String` message type. The
    # `chatter_callback` function is called whenever a new message is received.
    rospy.Subscriber('chatter', Localize, chatter_callback) 
    # Keeps the node running and listening for incoming messages on the subscribed topic.
    # The node will continue running until it is manually stopped.
    print("Waiting for messages...")
    rospy.spin()

if __name__ == '__main__':
    # Calls the function to start publishing messages to the topic.
    ekf = ExtendedKalmanFilter()
    listener()