cmake_minimum_required(VERSION 2.8.3)
project(baxter_challenge)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  baxter_core_msgs
  baxter_interface
  baxter_tools
  dynamic_reconfigure
  gazebo_msgs
  gazebo_ros
  geometry_msgs
  roscpp
  rospack
  rospy
  std_msgs
  actionlib_msgs
  message_generation
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
add_message_files(
  FILES
  BlockState.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  ObjectInspection.srv
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
)


###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS geometry_msgs roscpp rospy std_msgs message_runtime
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  ${catkin_INCLUDE_DIRS}
)
