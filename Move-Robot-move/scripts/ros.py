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


#画S，后退++前进+上半圆 + 下半圆+前进，半径都为0.25，前进0.25
def move_1():
    #创建发布信息的变量
    vel_msg = Twist()
    #设置旋转的角度,前进的距离
    distance_1 = 0.25
    distance_2 = 0.25
    change_arg = 3.1415926
    #设置前进的线速度与角速度
    arg = 0.5
    v = 0.125
    #得到需要信息的多少
    dt_1 = distance_1 / v 
    dt_2 = change_arg / arg
    dt_3 = distance_2 / v 

    #后退+前进+往左画一个半圆
    #后退
    vel_msg.linear.x = -v
    vel_s.publish(vel_msg)
    time.sleep(dt_1)

    sleep()

    #前进
    vel_msg.linear.x = v
    vel_s.publish(vel_msg)
    time.sleep(dt_1)

    sleep()

    #画圈
    vel_msg.linear.x = v
    vel_msg.angular.z = arg
    vel_s.publish(vel_msg)
    time.sleep(dt_2)
    
    sleep()

    #往右画一个半圆+前进
    #画圈
    vel_msg.linear.x = v
    vel_msg.angular.z = -arg
    vel_s.publish(vel_msg)
    time.sleep(dt_2)
    
    sleep()

    #前进
    vel_msg.linear.x = v
    vel_msg.angular.z = 0
    vel_s.publish(vel_msg)
    time.sleep(dt_3)

    sleep()
 


#画o，前进0.75m + 走一个半径为0.5的圆
def move_2():
    #创建发布信息的变量
    vel_msg = Twist()
    #设置前进的距离，旋转的角度
    distance = 0.75
    change_arg = 6.28318530716
    #设置前进的线速度与角速度
    arg = 1
    v = 0.5
    #得到需要信息的多少
    dt_1 = distance / v
    dt_2 = change_arg / arg

    #前进0.75m
    vel_msg.linear.x = v
    vel_cir.publish(vel_msg)
    time.sleep(dt_1)

    sleep()

    #走半径为0.5m的圆
    vel_msg.linear.x = v
    vel_msg.angular.z = -arg
    vel_cir.publish(vel_msg)
    time.sleep(dt_2)

    sleep()


#画r，前进1m，小圆转弯+前进1m + 后退0.5m 
def move_3():
    #创建发布信息的变量
    vel_msg = Twist()
    #设置向前走的距离，旋转的角度
    distance_1 = 1
    distance_2 = 0.65
    distance_3 = 1.25
    change_arg = 1.57079632679
    #设置前进的速度,旋转的角速度
    v = 0.2
    arg = 1
    #得到需要信息的多少
    dt_1 = distance_1 / v
    dt_2 = distance_2 / v
    dt_3 = change_arg / arg
    dt_4 = distance_3 / v

    #前进1.25m
    vel_msg.linear.x = v
    vel_pub.publish(vel_msg)
    time.sleep(dt_4)

    sleep()

    #小圆转弯,r=0.01
    vel_msg.linear.x = 0.01
    vel_msg.angular.z = -1
    vel_pub.publish(vel_msg)
    time.sleep(dt_3)

    sleep()

    #前进1m
    vel_msg.angular.z = 0
    vel_msg.linear.x = v
    vel_pub.publish(vel_msg)
    time.sleep(dt_1)

    sleep()
    
    #后退0.5m
    vel_msg.linear.x = -v
    vel_pub.publish(vel_msg)
    time.sleep(dt_2)

    sleep()


#转四分之一个圆，半径为0.65
def move_4():
    #创建发布信息的变量
    vel_msg = Twist()
    #设置旋转的角度
    change_arg = 1.57079632679
    #设置前进的线速度与角速度
    arg = 1
    v = 0.65
    #得到需要信息的多少
    dt_1 = change_arg / arg

    #开始旋转
    vel_msg.linear.x = v
    vel_msg.angular.z = -arg
    vel_arg.publish(vel_msg)
    time.sleep(dt_1)

    sleep()


if __name__ == '__main__':
    # ROS节点初始化
    rospy.init_node('draw_line')

    #创建每个环节的发布者对象
    vel_sleep = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_s = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_cir = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_arg = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    #等待建立连接
    time.sleep(3)

    #开始运动
    try:
        move_1()
        pass
    except rospy.ROSInterruptException:
        pass
    try:
        move_2()
        pass
    except rospy.ROSInterruptException:
        pass
    try:
        move_3()
        pass
    except rospy.ROSInterruptException:
        pass
    try:
        move_4()
        pass
    except rospy.ROSInterruptException:
        pass