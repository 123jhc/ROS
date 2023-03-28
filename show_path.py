#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from nav_msgs.msg import Odometry

from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

#定义轨迹发布器path_pub
path_pub = rospy.Publisher('robot_path',Path,queue_size=10)
#定义轨迹信息path_inform
path_infom = Path()

def get_odom(data):
	global path_infom
	global path_pub
	
	this_pose_stamped = PoseStamped()
	this_pose_stamped.pose.position = data.pose.pose.position
	this_pose_stamped.pose.orientation = data.pose.pose.orientation
	this_pose_stamped.header.frame_id = data.header.frame_id
	this_pose_stamped.header.stamp = data.header.stamp
	
	path_infom.header.frame_id = this_pose_stamped.header.frame_id
	path_infom.header.stamp = this_pose_stamped.header.stamp
	path_infom.poses.append(this_pose_stamped)

	path_pub.publish(path_infom)

def listener():
	rospy.init_node('robot_path_show', anonymous=True)
	odom_sub = rospy.Subscriber('/odom', Odometry , get_odom)
	rospy.loginfo('Start Show Robot path')
	rospy.spin()

	

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


