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

class Heading(smach.State):
    def __init__(self, smach_StateMachine, HEADING, TASK):
        self.HEADING = HEADING
        self.TASK = TASK
        self.sm = smach_StateMachine
        smach.State.__init__(self, outcomes=[self.TASK, 'aborted'])


    def addHeadingAction(self, g=None):
        if g is None:
            self.sm.add('HEADING', \
                                SimpleActionState('headingServer', \
                                headingAction, \
                                goal_cb=self.headingCallback), \
                                transitions={'succeeded':self.TASK,\
                                            'preempted':'HEADING',\
                                            'aborted':'aborted'})

        else:
            self.sm.add('HEADING_CONCURRENT', \
                                SimpleActionState('headingServer', \
                                headingAction, \
                                goal_cb=self.headingCallback), \
                                transitions={'succeeded':self.TASK,\
                                            'preempted':'HEADING_CONCURRENT',\
                                            'aborted':'aborted'})



    def headingCallback(self, userdata, goal):
        rospy.loginfo('Executing State New Heading')
        headingOrder = headingGoal()
        headingOrder.heading_setpoint = self.HEADING
        return headingOrder
