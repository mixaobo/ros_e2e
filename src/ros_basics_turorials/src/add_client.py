#!/usr/bin/env python2
import rospy
import sys
from ros_basics_turorials.srv import AddTwoInts
from ros_basics_turorials.srv import AddTwoIntsRequest
from ros_basics_turorials.srv import AddTwoIntsResponse


def add_two_ints_client(x, y):
    # Waits for the 'add_two_ints' service to become available before proceeding.
    rospy.wait_for_service('add_two_ints')
    try:
        # Creates a proxy object for the 'add_two_ints' service, allowing the client to call it.
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        
        # Calls the service with the provided integers `x` and `y`, and retrieves the response.
        response = add_two_ints(x, y)
        return response
    except rospy.ServiceException as e:
        # Prints an error message if the service call fails.
        print("Service call failed: %s" % e)


if __name__ == '__main__':
    # Checks if exactly two arguments (besides the script name) are provided via the command line.
    if len(sys.argv) == 3:
        # Converts the command-line arguments to integers.
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        # Prints usage instructions and exits if the required arguments are not provided.
        print("Usage: add_two_ints_client.py <a> <b>")
        sys.exit(1)
    
    # Logs the request being made to the service.
    print("Requesting %s + %s" % (a, b))
    
    # Calls the `add_two_ints_client` function to send the request and retrieve the result.
    s = add_two_ints_client(a, b)
    
    # Logs the result of the service call to the console.
    print("%s + %s = %s, test_value = %s" % (a, b, s.sum, s.testvalue))