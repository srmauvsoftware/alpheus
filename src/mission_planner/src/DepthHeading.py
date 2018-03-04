#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
import smach
import smach_ros
import actionlib
import alpheus_actions.msg

class Depth(smach.State):
    def __init__(self, PRESSURE):
        self.PRESSURE = PRESSURE
        smach.State.__init__(self, outcomes=['DepthReached'])

    def execute(self, ud):
        rospy.loginfo("Executing State Concurrent Depth")
        client = actionlib.SimpleActionClient('depthServer',\
                                            alpheus_actions.msg.depthAction)
        client.wait_for_server()
        goal = alpheus_actions.msg.depthGoal(depth_setpoint=self.PRESSURE)
        client.send_goal(goal)
        client.wait_for_result()
        result = client.get_state()
        if result == -1:
            return 'DepthReached'
        elif result == 'preempted':
            return 'aborted'
        elif result == 'aborted':
            return 'aborted'
        else: return 'aborted'

class Heading(smach.State):
    def __init__(self, HEADING):
        self.HEADING = HEADING
        smach.State.__init__(self, outcomes=['HeadingReached'])

    def execute(self, ud):
        rospy.loginfo("Executing State Concurrent Heading")
        client = actionlib.SimpleActionClient('headingServer',\
                                            alpheus_actions.msg.headingAction)
        client.wait_for_server()
        goal = alpheus_actions.msg.headingGoal(heading_setpoint=self.HEADING)
        client.send_goal(goal)
        client.wait_for_result()
        result = client.get_result()
        print(result)
        if result == -1:
            return 'HeadingReached'
        elif result == 'preempted':
            return 'aborted'
        elif result == 'aborted':
            return 'aborted'
        else: return 'aborted'

class DepthHeading():
    def __init__(self, PRESSURE, HEADING, TASK):
        self.PRESSURE = PRESSURE
        self.HEADING = HEADING
        self.TASK = TASK

    def addDepthHeading(self, sm):
        sm_con = smach.Concurrence(outcomes = ['DepthHeadingReached', 'DepthHeadingFailed'],
                                                default_outcome='DepthHeadingFailed',
                                                outcome_map={'DepthHeadingReached':
                                                {'DEPTH_CONCURRENT':'DepthReached',
                                                'HEADING_CONCURRENT':'HeadingReached'}})

        with sm_con:

            smach.Concurrence.add('DEPTH_CONCURRENT', Depth(self.PRESSURE))
            smach.Concurrence.add('HEADING_CONCURRENT', Heading(self.HEADING))


        smach.StateMachine.add('DEPTH+HEADING', sm_con, transitions={
                                    'DepthHeadingFailed':'DEPTH+HEADING',
                                    'DepthHeadingReached':self.TASK })
