#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from smach import StateMachine
from geometry_msgs.msg import Pose2D
from alpheus_actions.msg import depthGoal
from rospy.exceptions import ROSInitException
from rospy.timer import Rate
import smach
from smach_ros import SimpleActionState
import time

class sink(smach.State):
    def __init__(self, ip, depth):
        self.INITIAL_PRESSURE = ip
        self.Y_OFFSET = depth

    def execute(self, userdata):
        rospy.loginfo('State - Sink Alpheus')
        rospy.loginfo("Going to : %f", INITIAL_PRESSURE)


def main():
    rospy.init_node('sink_state')
    sm = smach.StateMachine(outcomes=['sink', 'not-sink'])

    with sm:
        def sink_goal_callback(goal):
            depthOrder = depthGoal()
            depthOrder.depth_setpoint = goal
            return depthOrder

        StateMachine.add('SINK_ALPHEUS', \
            SimpleActionState(), \
            transitions={'succeeded':''})
