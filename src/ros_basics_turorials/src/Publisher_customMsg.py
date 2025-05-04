#!/usr/bin/env python2
import rospy
from ros_basics_turorials.msg import CustomMsg

def Pubs_customMsg():
    # Creates a publisher object for the topic 'Sensor_Topic', which uses the `CustomMsg` message type.
    # The `queue_size=10` ensures that up to 10 messages are buffered before being processed by subscribers.
    pub = rospy.Publisher('Sensor_Topic', CustomMsg, queue_size=10) 
    
    # Initializes the ROS node with the name 'Publisher_node'. The `anonymous=True` argument ensures
    # that if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('Publisher_node', anonymous=True)

    # Sets the rate at which the loop will run. Here, the loop will execute once per second (1 Hz).
    rate = rospy.Rate(1)

    # A counter variable used to modify the message content in each iteration.
    i = 0
    while not rospy.is_shutdown():
        # Creates an instance of the `CustomMsg` message type and assigns values to its fields.
        iot_sensor = CustomMsg()
        iot_sensor.id = 1 + i
        iot_sensor.name = "Temperature + %d" % i
        
        # Logs the message content to the console for debugging or monitoring purposes.
        rospy.loginfo(iot_sensor)
        
        # Publishes the message to the 'Sensor_Topic' topic so that subscribers can receive it.
        pub.publish(iot_sensor)
        
        # Pauses the loop for the duration specified by the rate (1 second in this case).
        rate.sleep()

        # Increments the counter to modify the message content in the next iteration.
        i += 1


if __name__ == '__main__':
    try:
        # Calls the function to start publishing messages to the topic.
        Pubs_customMsg()
    except rospy.ROSInterruptException:
        # Handles the exception if the ROS node is interrupted (e.g., by pressing Ctrl+C).
        pass