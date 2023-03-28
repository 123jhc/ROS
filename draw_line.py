#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy,math
from geometry_msgs.msg import Twist,Point
from nav_msgs.msg import Odometry

current_positon = Point()
#定义当前位置和起始位置的差值
target_distance = 1.0

min_velocity = 0.05
max_velocity = 0.3

#订阅里程计信息
def get_odom(data):
	global current_positon
	current_positon = data.pose.pose.position

def velocity_publisher():
	global target_distance
	# ROS节点初始化
	rospy.init_node('draw_line', anonymous=True)

	# 创建一个Publisher，发布名为/cmd_vel的topic，消息类型为geometry_msgs::Twist，队列长度10
	vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

	odom_sub = rospy.Subscriber('/odom', Odometry , get_odom)
	#设置循环的频率
	rate = rospy.Rate(10) 

	vel_msg = Twist()
	rospy.loginfo("Start Control Robot Draw Line.")
	forward_flag = True

	while not rospy.is_shutdown():
		
		start_position = current_positon
		while True:
			#计算当前已行走直线距离和目标直线距离之差
			differ = target_distance - ((current_positon.x - start_position.x)**2 + (current_positon.y - start_position.y)**2)**0.5
			if(differ > 0):
				vel_msg.linear.x = math.sin(differ*3.14)
   	  			
				if vel_msg.linear.x < min_velocity:
					vel_msg.linear.x = min_velocity
				if vel_msg.linear.x > max_velocity:
					vel_msg.linear.x = max_velocity

				if not forward_flag:
					vel_msg.linear.x *= -1.0
				else:
					pass

		  		# 发布消息
        	  		vel_pub.publish(vel_msg)
    		  	else:
				vel_msg.linear.x = 0.0
				vel_pub.publish(vel_msg)
				break

		 	# 按照循环频率延时
        	 	rate.sleep()
			
		forward_flag = bool(1-forward_flag)


if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass


