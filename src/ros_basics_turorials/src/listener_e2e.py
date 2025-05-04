#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

def chatter_callback(msg):
    # Logs the message received on the 'chatter' topic along with the caller ID of the node.
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", msg.data)

def listener():
    # Initializes a ROS node named 'listener'. The `anonymous=True` argument ensures that
    # if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('listener', anonymous=True)
    
    # Subscribes to the 'chatter' topic, which uses the `String` message type. The
    # `chatter_callback` function is called whenever a new message is received.
    rospy.Subscriber('chatter', String, chatter_callback)
    
    # Keeps the node running and listening for incoming messages on the subscribed topic.
    # The node will continue running until it is manually stopped.
    rospy.spin()

if __name__ == '__main__':
    # Entry point of the script. Calls the `listener` function to start the node.
    listener()