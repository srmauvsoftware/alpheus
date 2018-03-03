#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from Depth import Depth
from Heading import Heading
import smach
import smach_ros

class DepthHeading(smach.State):
    def __init__(self, smach_StateMachine, PRESSURE, HEADING, TASK):
        self.PRESSURE = PRESSURE
        self.HEADING = HEADING
        self.TASK = TASK
        self.sm = smach_StateMachine
        smach.State.__init__(self, outcomes=[self.TASK])

        self.sm_con = smach.Concurrence(outcomes = ['DepthHeadingReached', 'DepthHeadingFailed'],
                                                default_outcome='DepthHeadingFailed',
                                                outcome_map={'DepthHeadingReached':
                                                {'DEPTH_CONCURRENT':'DepthReached',
                                                'HEADING_CONCURRENT':'HeadingReached'}})
        with self.sm_con:
            self.depthTask = Depth(self.sm_con, self.PRESSURE, 'DepthReached')
            smach.Concurrence.add('DEPTH_CONCURRENT', self.depthTask)
            self.headingTask = Heading(self.sm_con, self.HEADING, 'HeadingReached')
            smach.Concurrence.add('HEADING_CONCURRENT', self.headingTask)

    def addDepthHeading(self):
        self.sm.add('DEPTH+HEADING',self.sm_con,transitions={
                                    'DepthHeadingFailed':'DEPTH+HEADING',
                                    'DepthHeadingReached':self.TASK })

    def startDepthHeading(self):
        self.headingTask.addHeadingAction(g = 'Concurrence')
        self.depthTask.addDepthAction(g = 'Concurrence')
