#!/bin/bash

# Install ROS and Catkin
rosdep update
sudo apt-get update
sudo apt-get dist-upgrade 
sudo apt-get install ros-kinetic-catkin python-catkin-tools
# Install MoveIt!
sudo apt install ros-kinetic-moveit
# Create A Catkin Workspace
mkdir -p ~/ws_moveit/src
# Download the Example Code
cd ~/ws_moveit/src
git clone https://github.com/ros-planning/moveit_tutorials.git
git clone https://github.com/ros-planning/panda_moveit_config.git
# Build your Catkin Workspace
cd ~/ws_moveit/src
sudo apt-get update
rosdep install -y --from-paths . --ignore-src --rosdistro kinetic
cd ~/ws_moveit
catkin config --extend /opt/ros/kinetic
catkin build
source ~/ws_moveit/devel/setup.bash
echo 'source ~/ws_moveit/devel/setup.bash' >> ~/.bashrc
