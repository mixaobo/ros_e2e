#!/usr/bin/env python2
import rospy
from std_msgs.msg import String

def talker():
    # Creates a publisher object for the topic 'chatter', which uses the `String` message type.
    # The `queue_size=10` ensures that up to 10 messages are buffered before being processed by subscribers.
    pub = rospy.Publisher('chatter', String, queue_size=10) 
    
    # Initializes the ROS node with the name 'talker'. The `anonymous=True` argument ensures
    # that if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('talker', anonymous=True)

    # Sets the rate at which the loop will run. Here, the loop will execute once per second (1 Hz).
    rate = rospy.Rate(1)

    # A counter variable used to modify the message content in each iteration.
    i = 0
    while not rospy.is_shutdown():
        # Creates a string message with a counter value appended to "hello world".
        hello_str = "hello world %s" % i
        
        # Logs the message content to the console for debugging or monitoring purposes.
        rospy.loginfo(hello_str)
        
        # Publishes the message to the 'chatter' topic so that subscribers can receive it.
        pub.publish(hello_str)
        
        # Pauses the loop for the duration specified by the rate (1 second in this case).
        rate.sleep()

        # Increments the counter to modify the message content in the next iteration.
        i += 1


if __name__ == '__main__':
    try:
        # Calls the function to start publishing messages to the topic.
        talker()
    except rospy.ROSInterruptException:
        # Handles the exception if the ROS node is interrupted (e.g., by pressing Ctrl+C).
        pass