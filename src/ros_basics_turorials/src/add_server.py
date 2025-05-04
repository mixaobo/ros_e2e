#!/usr/bin/env python2
import rospy
from ros_basics_turorials.srv import AddTwoInts
from ros_basics_turorials.srv import AddTwoIntsRequest
from ros_basics_turorials.srv import AddTwoIntsResponse

def add_two_ints_server_cbk(msg):
    # This function is the callback for the service. It receives a request of type AddTwoIntsRequest,
    # extracts the integers `a` and `b` from the request, computes their sum, and returns a response
    # of type AddTwoIntsResponse containing the result.
    print ("Request received: %s + %s = %s," % (msg.a, msg.b, msg.a + msg.b))
    retVal = AddTwoIntsResponse()
    retVal.sum = msg.a + msg.b
    retVal.testvalue = 1024
    return AddTwoIntsResponse(retVal.sum, retVal.testvalue)

def add_two_ints_server():
    # Initializes the ROS node with the name 'add_two_ints_server'. The `anonymous=True` argument ensures
    # that if multiple instances of this node are launched, they will have unique names.
    rospy.init_node('add_two_ints_server', anonymous=True)
    
    # Creates a service named 'add_two_ints' of type AddTwoInts. When a request is received, the
    # `add_two_ints_server_cbk` function is called to process the request and generate a response.
    s = rospy.Service('add_two_ints', AddTwoInts, add_two_ints_server_cbk)
    
    # Keeps the node running and listening for incoming service requests. The node will continue
    # running until it is manually stopped.
    rospy.spin()

if __name__ == '__main__':
    # Entry point of the script. Calls the `add_two_ints_server` function to start the service.
    add_two_ints_server()