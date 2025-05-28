#!/usr/bin/env python2
import rospy
import numpy as np
from ros_basics_turorials.msg import Localize
from scipy.optimize import least_squares

def node_server_callback(msg):
    parsed_msg = Localize()
    parsed_msg.Distance = msg.Distance
    parsed_msg.AoA = msg.AoA
    print("node_server received msg: ", parsed_msg)
    

def Node_server():
    global pub_server
    #Initialize
    rospy.init_node('node_server', anonymous=True)

    # subscribe to node_localize
    rospy.Subscriber('topic_localize', Localize, node_server_callback)
    rospy.spin()



if __name__ == '__main__':
    Node_server()
