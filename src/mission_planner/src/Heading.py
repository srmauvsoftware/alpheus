#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from smach import StateMachine
from alpheus_actions.msg import headingGoal, headingAction
import alpheus_actions.msg
from rospy.exceptions import ROSInitException
from rospy.timer import Rate
import smach
import actionlib
from smach_ros import SimpleActionState
import time

class Heading():
    def __init__(self, smach_StateMachine, HEADING):
        self.HEADING = HEADING
        smach_StateMachine.add('GOTO_HEADING', \
                                SimpleActionState('headingServer', \
                                headingAction, \
                                goal_cb=self.headingCallback), \
                                transitions={'succeeded':'mission_complete',\
                                            'preempted':'not-sink',\
                                            'aborted':'not-sink'})


    def headingCallback(self, userdata, goal):
        rospy.loginfo('Executing State New Heading')
        headingOrder = headingGoal()
        headingOrder.heading_setpoint = self.HEADING
        return headingOrder
