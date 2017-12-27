#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Quaternion


def talker():
    pub = rospy.Publisher('/imu_data', Imu, queue_size=10)
    rospy.init_node('IMU_TEST_NODE', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        msg = Imu()
        orientation = Quaternion()
        orientation.x = 0.0
        orientation.y = 0.0
        orientation.z = 0.0
        orientation.w = 0.0
        msg.orientation = orientation
        angular_velocity = Vector3()
        angular_velocity.x = 0.0
        angular_velocity.y = 0.0
        angular_velocity.z = 0.0
        msg.angular_velocity = angular_velocity
        linear_acceleration = Vector3()
        linear_acceleration.x = 0.0
        linear_acceleration.y = 0.0
        linear_acceleration.z = 0.0
        msg.linear_acceleration = linear_acceleration
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
