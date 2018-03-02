#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from Depth import Depth
from Heading import Heading
import smach
import smach_ros

class DepthHeading():
    def __init__(self, smach_StateMachine, PRESSURE, HEADING, TASK):
        self.PRESSURE = PRESSURE
        self.HEADING = HEADING

        sm_con = smach.Concurrence(outcomes = ['DepthHeadingReached', 'DepthHeadingFailed'],
                                                default_outcome='DepthHeadingFailed',
                                                outcome_map={'DepthHeadingReached':
                                                {'Depth':'DepthReached',
                                                'Heading':'HeadingReached'}})

        with sm_con:
            smach.Concurrence.add('Heading', Heading(smach_StateMachine, self.HEADING, 'DepthReached'))
            smach.Concurrence.add('Depth', Depth(smach_StateMachine, self.PRESSURE, 'HeadingReached'))

        smach_StateMachine.add('DEPTH+HEADING',sm_con,transitions={
                                    'DepthHeadingFailed':'DEPTH+HEADING',
                                    'DepthHeadingReached':TASK })
