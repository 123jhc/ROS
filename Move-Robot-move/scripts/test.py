#!/usr/bin/env python
#coding=utf-8

import rospy
from geometry_msgs.msg import Twist
import time

#休眠函数，每运动一次，休眠一秒
def sleep():
    sleep_msg = Twist()
    sleep_msg.linear.x = 0
    sleep_msg.angular.z = 0
    vel_sleep.publish(sleep_msg)
    time.sleep(1)


#r=0.1
def move_1():
    #创建发布信息的变量
    vel_msg = Twist()
    #设置旋转的角度,前进的距离
    change_arg = 1.5707963
    #设置前进的线速度与角速度
    arg = 1
    v = 0.1
    #得到需要信息的多少
    dt_1 = change_arg / arg

    vel_msg.linear.x = v
    vel_msg.angular.z = arg
    vel_1.publish(vel_msg)
    time.sleep(dt_1)

    sleep()



if __name__ == '__main__':
    # ROS节点初始化
    rospy.init_node('draw_line')

    #创建每个环节的发布者对象
    vel_sleep = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    #等待建立连接
    time.sleep(3)

    #开始运动
    try:
        move_1()
        pass
    except rospy.ROSInterruptException:
        pass
