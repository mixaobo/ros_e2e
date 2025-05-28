#!/usr/bin/env python2
import socket
import rospy
from e2e_hpc.msg import CustomMsg_Ranging

# Configuration for the TCP server
HOST = '0.0.0.0' # Listen on all interfaces (replace with anchor IP if needed)
PORT = 8888      # Port to listen on (replace with anchor port if needed)

def parse_string_data(data):
    """
    Parse the received string data in the format:
    ble_status(string)/firstPath_power(float)/aoa(float)/distance(float)
    Example: "Connected/12.34/56.78/9.01"
    Returns a dictionary with parsed values or None if parsing fails.
    """
    try:
        fields = data.split('/')
        parsed_data = {
            'ble_status': fields[0],
            'firstPath_power': float(fields[1]),
            'aoa': float(fields[2]),
            'distance': float(fields[3])
        }
        return parsed_data
    except (IndexError, ValueError) as e:
        rospy.logerr("Failed to parse string data: {}. Data: {}".format(e, data))
        return None

def populate_message(msg_type, parsed_data):
    """
    Populate a ROS message of type msg_type with values from parsed_data.
    Only sets fields that exist in both the message and the parsed data.
    """
    msg = msg_type()
    for field in msg.__slots__:
        if field in parsed_data:
            setattr(msg, field, parsed_data[field])
    return msg

def start_node_ethernet():
    # Initialize the ROS node
    rospy.init_node('node_ethernet', anonymous=True)
    rospy.loginfo("Node Ethernet Started.")

    # Create a ROS publisher for the ranging topic
    ranging_pub = rospy.Publisher('topic_ranging', CustomMsg_Ranging, queue_size=10)

    # Create and configure the TCP server socket
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(5)
        rospy.loginfo("Node ethernet is listening on {}:{}".format(HOST, PORT))

        # Main server loop: accept new connections
        while not rospy.is_shutdown():
            try:
                srv.settimeout(1.0)  # Timeout to allow ROS shutdown checks
                try:
                    conn, addr = srv.accept()  # Wait for a client connection
                except socket.timeout:
                    continue  # No connection, check for shutdown and continue

                srv.settimeout(None)
                rospy.loginfo("Accepted connection from {}".format(addr))
                buffer = b''  # Buffer for incoming data

                # Connection loop: receive and process data from the client
                while not rospy.is_shutdown():
                    conn.settimeout(1.0)  # Timeout for receiving data
                    try:
                        data = conn.recv(4096)  # Receive up to 4096 bytes
                    except socket.timeout:
                        continue  # No data, check for shutdown and continue
                    conn.settimeout(None)

                    if not data:
                        # Client disconnected
                        rospy.loginfo("Client {} disconnected.".format(addr))
                        break

                    buffer += data  # Append received data to buffer

                    # Process all complete lines in the buffer
                    while b'\n' in buffer:
                        line, buffer = buffer.split(b'\n', 1)
                        if not line:
                            continue  # Skip empty lines

                        try:
                            rospy.loginfo("Received string data from {}: {}".format(addr, line))
                            parsed_data = parse_string_data(line.decode('utf-8'))
                            if parsed_data:
                                # Create and publish the ROS message
                                ranging_msg = populate_message(CustomMsg_Ranging, parsed_data)
                                ranging_pub.publish(ranging_msg)
                                rospy.loginfo("Published ranging message: \n{}".format(ranging_msg))
                        except Exception as e:
                            rospy.logerr("Error processing message from {}: {}".format(addr, e))

            except socket.error as e:
                # Handle socket errors (e.g., address in use)
                if not rospy.is_shutdown():
                    rospy.logerr("Socket error in main loop: {}".format(e))
                if e.errno == 98:
                    rospy.logfatal("Address already in use. Shutting down node ethernet.")
                    break
            except Exception as e:
                # Handle other exceptions (e.g., ROS shutdown)
                if not rospy.is_shutdown():
                    rospy.loginfo("Node ethernet interrupted.")
                break

    except Exception as e:
        # Handle any unhandled exceptions during setup or main loop
        rospy.logerr("Unhandled exception in node ethernet: {}".format(e))
    finally:
        # Always close the server socket on exit
        srv.close()
        rospy.loginfo("Node ethernet is shutting down.")

if __name__ == '__main__':
    try:
        # Uncomment the next line to run the test publisher instead of the socket server:
        # test_publisher()
        start_node_ethernet()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node ethernet is interrupted.")
    except Exception as e:
        rospy.logerr("Unhandled exception in node ethernet: {}".format(e))