#! /usr/bin/env python
import rospy
from alpheus_msgs.msg import depthThruster
from alpheus_msgs.msg import vectorThruster
import threading

def depthTalker():
    pub = rospy.Publisher('/thruster/depth', depthThruster, queue_size=10)
    rospy.init_node('depth_thruster_test_node', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = depthThruster()
        msg.td1 = 1500
        msg.td2 = 1500
        msg.td3 = 1500
        msg.td4 = 1500
        pub.publish(msg)
        rate.sleep()

def vectorTalker():
    pub = rospy.Publisher('/thruster/vector', vectorThruster, queue_size=10)
    rospy.init_node('vector_thruster_test_node', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = vectorThruster()
        msg.tfr = 1500
        msg.tfl = 1500
        msg.trl = 1500
        msg.trr = 1500
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        dt = threading.Thread(target=depthTalker)
        vt = threading.Thread(target=vectorTalker)
        dt.start()
        vt.start()
    except rospy.ROSInterruptException:
        pass
