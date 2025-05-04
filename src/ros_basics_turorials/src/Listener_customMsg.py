#!/usr/bin/env python2
import rospy
from ros_basics_turorials.msg import CustomMsg

def chatter_callback(msg):
    # This function is triggered whenever a message is received on the 'Sensor_Topic' topic.
    # It creates a new instance of the `CustomMsg` message type, assigns the received data
    # (id and name) to it, and logs the message to the console.
    parsedata = CustomMsg()
    parsedata.id = msg.id
    parsedata.name = msg.name
    rospy.loginfo("I heard %s", parsedata)

def listener():
    # Initializes a ROS node named 'Listener_node'. The `anonymous=True` argument ensures
    # that if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('Listener_node', anonymous=True)
    
    # Subscribes to the 'Sensor_Topic' topic, which uses the `CustomMsg` message type.
    # The `chatter_callback` function is called whenever a new message is received.
    rospy.Subscriber('Sensor_Topic', CustomMsg, chatter_callback)
    
    # Keeps the node running and listening for incoming messages on the subscribed topic.
    # The node will continue running until it is manually stopped.
    rospy.spin()

if __name__ == '__main__':
    # Entry point of the script. Calls the `listener` function to start the node.
    listener()