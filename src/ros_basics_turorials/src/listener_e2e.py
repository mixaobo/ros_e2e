import rospy
from std_msgs import String

def talker():
    pub = rospy.Publisher('Chatter', String, queue_size=10) #Topic_name, type
    


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass