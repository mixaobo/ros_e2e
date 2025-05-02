import rospy
from std_msgs.msg import String

def chatter_callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
    

def listener():
    #Initialize the node: Name, anonymous=True means that if multiple nodes are running, they will have unique names
    rospy.init_node('listener', anonymous=True)
    #Define topic name, data type, queue for topic message before listener consumes
    rospy.Subscriber('chatter', String, chatter_callback)
    #Start listening to the topic #keeps the node from exiting until the node is stopped
    rospy.spin() 




if __name__ == '__main__':
    listener()