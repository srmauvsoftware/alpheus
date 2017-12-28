#! /usr/bin/env python
import rospy
import actionlib
import alpheus_actions.msg
from geometry_msgs.msg import Pose2D

class headingAction(object):
    _feedback = alpheus_actions.msg.headingFeedback()
    _result = alpheus_actions.msg.headingResult()

    def __init__(self, name):
        rospy.Subscriber("/imu/HeadingTrue_degree", Pose2D, self.heading_cb)
        self._ha = name
        self._hs = actionlib.SimpleActionServer(
            self._ha, \
            alpheus_actions.msg.headingAction, \
            execute_cb = self.headingCallback, \
            auto_start = False)
        self._hs.start()

    def heading_cb(self, data):
        if(data.theta < 0):
            self.heading_value = 360 + data.theta
        else:
            self.heading_value = data.theta

    def headingCallback(self, goal):
        r = rospy.Rate(10)
        success = True

        while(goal.heading_setpoint != self.heading_value):
            if self._hs.is_preempt_requested():
                rospy.loginfo('%s : Preempted' % self._ha)
                self._hs.set_preempted()
                success = False
                break
            self._feedback.heading_error = self.heading_value
            self._hs.publish_feedback(self._feedback)
            self._feedback.heading_error = self._heading_value - goal.heading_setpoint
            rospy.loginfo('%s : Going to Heading %f with Error : %f',\
                self._ha, \
                goal.heading_setpoint, \
                self._feedback.heading_error)

            r.sleep()

        if success:
            self._result.heading_final = self._feedback.heading_error
            rospy.loginfo('%s : Success' % self._ha)
            self._ds.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('headingServer')
    server = headingAction(rospy.get_name())
    rospy.spin()
