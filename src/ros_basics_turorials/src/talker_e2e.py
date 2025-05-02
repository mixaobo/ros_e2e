#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

def talker():
    #Define topic name, data type, queue for topic message before listener consumes
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    
    #Initialize the node: Name, anonymous=True means that if multiple nodes are running, they will have unique names
    rospy.init_node('talker', anonymous=True)

    #Set the rate at which the loop will run
    rate = rospy.Rate(1) # 10hz

    #Publish messages in a loop
    i = 0
    while not rospy.is_shutdown():
        #Create a message
        hello_str = "hello world %s" % i
        
        #Log the message to the console
        rospy.loginfo(hello_str)
        
        #Publish the message to the topic
        pub.publish(hello_str)
        
        #Sleep for the specified rate
        rate.sleep()

        #Increment the counter
        i += 1


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass