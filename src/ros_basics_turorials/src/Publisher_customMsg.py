#!/usr/bin/env python2
import rospy
from ros_basics_turorials.msg import CustomMsg

def Pubs_customMsg():
    #Define topic name, data type, queue for topic message before listener consumes
    pub = rospy.Publisher('Sensor_Topic', CustomMsg, queue_size=10) 
    
    #Initialize the node: Name, anonymous=True means that if multiple nodes are running, they will have unique names
    rospy.init_node('Publisher_node', anonymous=True)

    #Set the rate at which the loop will run
    rate = rospy.Rate(1) # 10hz

    #Publish messages in a loop
    i = 0
    while not rospy.is_shutdown():
        #Create a message
        iot_sensor = CustomMsg()
        iot_sensor.id = 1 + i
        iot_sensor.name = "Temperature + %d" % i
        
        #Log the message to the console
        rospy.loginfo(iot_sensor)
        
        #Publish the message to the topic
        pub.publish(iot_sensor)
        
        #Sleep for the specified rate
        rate.sleep()

        #Increment the counter
        i += 1


if __name__ == '__main__':
    try:
        Pubs_customMsg()
    except rospy.ROSInterruptException:
        pass