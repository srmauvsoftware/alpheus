#! /usr/bin/env python
import rospy
from alpheus_msgs.msg import thruster

def talker():
    pub = rospy.Publisher('/thruster', thruster, queue_size=10)
    rospy.init_node('thruster_test_node', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = thruster()
        msg.speedfwd1 = 1900
        msg.speedfwd2 = 1500
        msg.speedup1 = 1500
        msg.speedup2 = 1500
        msg.speedup3 = 1500
        msg.speedup4 = 1500
        msg.speeddir1 = 1500
        msg.speeddir2 = 1500
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
