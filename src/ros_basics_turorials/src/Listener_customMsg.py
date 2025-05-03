#!/usr/bin/env python2
import rospy
from ros_basics_turorials.msg import CustomMsg

def chatter_callback(msg):
    parsedata = CustomMsg()
    #Create a message
    parsedata.id = msg.id
    parsedata.name = msg.name
    #Log the message to the console
    rospy.loginfo("I heard %s", parsedata)

    

def listener():
    #Initialize the node: Name, anonymous=True means that if multiple nodes are running, they will have unique names
    rospy.init_node('Listener_node', anonymous=True)
    #Define topic name, data type, queue for topic message before listener consumes
    rospy.Subscriber('Sensor_Topic', CustomMsg, chatter_callback)
    #Start listening to the topic #keeps the node from exiting until the node is stopped
    rospy.spin() 




if __name__ == '__main__':
    listener()