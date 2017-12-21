#! /usr/bin/env python
import rospy
from alpheus_msgs.msg import pressure

def talker():
    pub = rospy.Publisher('/pressure', pressure, queue_size=10)
    rospy.init_node('pressure_node', anonymous=True)
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
        msg = pressure()
        msg.pressure = i
        i = i + 1
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
