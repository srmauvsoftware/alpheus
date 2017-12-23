#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from smach import StateMachine
from geometry_msgs.msg import Pose2D
from alpheus_actions.msg import depthGoal
import alpheus_actions.msg
from rospy.exceptions import ROSInitException
from rospy.timer import Rate
import smach
import actionlib
from smach_ros import SimpleActionState
import time

INITIAL_PRESSURE = 520

def main():
    rospy.init_node('sink_state')
    sm = smach.StateMachine(outcomes=['sink', 'not-sink'])

    with sm:
        def sink_goal_callback(self, goal):
            depthOrder = depthGoal()
            depthOrder.depth_setpoint = INITIAL_PRESSURE
            return depthOrder

        StateMachine.add('SINK_ALPHEUS', \
            SimpleActionState('depthServer',\
                alpheus_actions.msg.depthAction, \
                goal_cb = sink_goal_callback,), \
            transitions={'succeeded':'sink',\
                        'preempted':'sink',\
                        'aborted':'sink'})

    outcome = sm.execute()

if __name__ == '__main__':
    main()
