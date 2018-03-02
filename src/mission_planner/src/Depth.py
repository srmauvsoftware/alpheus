#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from smach import StateMachine
from alpheus_actions.msg import depthGoal, depthAction
import alpheus_actions.msg
from rospy.exceptions import ROSInitException
from rospy.timer import Rate
import smach
import actionlib
from smach_ros import SimpleActionState
import time

class Depth():
    def __init__(self, smach_StateMachine, PRESSURE, TASK):
        self.PRESSURE = PRESSURE
        smach_StateMachine.add('DEPTH', \
                                SimpleActionState('depthServer', \
                                depthAction, \
                                goal_cb=self.depthCallback), \
                                transitions={'succeeded':TASK,\
                                            'preempted':'DEPTH',\
                                            'aborted':'not-sink'})


    def depthCallback(self, userdata, goal):
        rospy.loginfo('Executing State New Depth')
        depthOrder = depthGoal()
        depthOrder.depth_setpoint = self.PRESSURE
        return depthOrder
