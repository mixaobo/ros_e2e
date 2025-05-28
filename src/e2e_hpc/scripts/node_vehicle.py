#!/usr/bin/env python2
import rospy
from ros_basics_turorials.msg import CustomMsg_Door
from ros_basics_turorials.msg import CustomMsg_Ranging
from ros_basics_turorials.msg import CustomMsg_Connection

def Connection_callback(msg):
  """#Handle vehicle status
  VehicleStatus: "Sleep", "Awake"
  BleStatus: "Connected", "Disconnected"
  UWBStatus: "NA", "Ranging", "CPD", "Mixed"
  """
  print("Connection_callback")
  pass

def Localization_callback(msg):
  """Handle DOORS status based on distance and angle of arrival (AoA)
  FrontLeft: ["open"/"closed", "locked"/"unlocked"]
  FrontRight: ["open"/"closed", "locked"/"unlocked"]
  RearLeft: ["open"/"closed", "locked"/"unlocked"]
  RearRight: ["open"/"closed", "locked"/"unlocked"]
  """
  print("Localization_callback")
  pass

def Node_vehicle():
    global pub_Door, pub_Connection
    #Initialize
    rospy.init_node('node_Vehicle', anonymous=True)

    #Publish to
    pub_Door = rospy.Publisher('topic_Door', CustomMsg_Door, queue_size=10)
    pub_Connection = rospy.Publisher('topic_Connection', CutsomMsg_Connection, queue_size=10)

    #Subscribe to
    rospy.Subscriber('topic_Connection', CutsomMsg_Connection, Connection_callback)
    rospy.Subscriber('topic_Localization', CustomMsg_Ranging, Localization_callback)
    rospy.spin()

if __name__ == '__main__':
    Node_vehicle()
