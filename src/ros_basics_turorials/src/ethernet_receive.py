#!/usr/bin/env python2
import rospy
import socket
from std_msgs.msg import String

def ethernet_listener():
    # Initialize the ROS node
    rospy.init_node('Ethernet_Listener_node', anonymous=True)

    # Create a publisher to the 'ethernet_data' topic
    publisher = rospy.Publisher('ethernet_data', String, queue_size=10)

    # Ethernet connection details
    ip = "127.0.0.1"  # Replace with your Ethernet device's IP address
    port = 12345  # Replace with your Ethernet device's port number

    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)
    rospy.loginfo("Listening for data on %s:%d", ip, port)

    while not rospy.is_shutdown():
        rospy.loginfo("Waiting for a new connection...")
        # Accept a connection from the client
        conn, addr = sock.accept()
        rospy.loginfo("Connection established with %s", addr)

        while not rospy.is_shutdown():
            try:
                # Receive data from the Ethernet device
                data = conn.recv(1024)  # Buffer size is 1024 bytes
                if not data:
                    rospy.loginfo("Connection closed by client")
                    break  # Exit the inner loop to accept a new connection
                # Decode the received data and publish it to the 'ethernet_data' topic
                decoded_data = data.decode('utf-8')
                rospy.loginfo("Received data: %s", decoded_data)
                publisher.publish(decoded_data)
            except socket.error as e:
                rospy.logerr("Socket error: %s", e)
                break  # Exit the inner loop to accept a new connection

        # Close the connection and wait for a new client
        conn.close()
        rospy.loginfo("Socket connection closed")

    # Close the server socket when the node is shut down
    sock.close()
    rospy.loginfo("Server socket closed")


if __name__ == '__main__':
    # Entry point of the script. Calls the `ethernet_listener` function to start the node.
    ethernet_listener()