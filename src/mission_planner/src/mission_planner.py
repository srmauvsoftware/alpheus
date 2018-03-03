#! /usr/bin/env python
import roslib; roslib.load_manifest('mission_planner')
import rospy
from smach import StateMachine
from rospy.exceptions import ROSInitException
from rospy.timer import Rate
import smach
import time
from smach_ros import IntrospectionServer
from Sink import Sink
from Depth import Depth
from Heading import Heading
from DepthHeading import DepthHeading

def main():
    rospy.init_node('mission_planner')
    sm = smach.StateMachine(outcomes=['mission_complete', 'mission_failed', 'aborted'])

    with sm:
        Sink(sm, 200, 'DEPTH')
        Depth(sm, 300, 'HEADING')
        Heading(sm, 400, 'mission_complete')
        #DepthHeading(sm, 500, 600, 'mission_complete')
        sis = IntrospectionServer('ALPHEUS_MISSION_PLANNER', sm, '/START_ALPHEUS')
        sis.start()
        outcome = sm.execute()


    rospy.spin()
    sis.stop()
if __name__ == '__main__':
    main()
