#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Pose2D

def talker():
    pub = rospy.Publisher('/imu/HeadingTrue_degree', Pose2D, queue_size=10)
    rospy.init_node('heading_test', anonymous=True)
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
        msg = Pose2D()
        msg.theta = i
        i = i + 1
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
