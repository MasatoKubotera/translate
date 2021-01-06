cmake_minimum_required(VERSION 3.0.2)
project(translate)


find_package(catkin REQUIRED COMPONENTS
  rospy
)


###########
## Build ##
###########

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)