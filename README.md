# ros_e2e

Create project
1. Setup environment
  - gedit ~/.bashrc
  - add "source /opt/ros/melodic/setup.bash" to the file
  - add "<your_workspace_path>/devel/setup.bash" to the file
  - Run source ~/.bashrc if new ROS packaged is created
2. Create new ROS project
  - mkdir -p ~/catkin_ws/src (will create parent folder if it's not exist)
3. build your ROS workspace
  - ~/catkin_ws$ catkin_make

Create new ROS package
1. catkin_create_pkg <pkg_name> rospy roscpp std_msgs #library, dependencies, ...
2. Add new python file under <pkg_name><pkg_name>/src
  # Install Python scripts
  catkin_install_python(PROGRAMS
    src/listener_e2e.py
    src/talker_e2e.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
  )
3. Compile again with catkin_make

How to run.
1. Run master node: roscore
2. Run node: rosrun <pkg_name> <node_name>

Create custom Message
1. Add new_file.msg
2. Update Cmake
  find_package(catkin REQUIRED COMPONENTS
    roscpp
    rospy
    std_msgs
    message_generation
  )

  add_message_files(
    FILES
    CustomMsg.msg
  )
3. update package.xml
    <build_depend>message_generation</build_depend>
    <exec_depend>message_generation</exec_depend>





