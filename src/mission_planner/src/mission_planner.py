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

def main():
    rospy.init_node('mission_planner')
    sm = smach.StateMachine(outcomes=['mission_complete', 'mission_failed', 'not-sink', 'heading_success'])

    with sm:
        Sink(sm, 200)
        Depth(sm, 300)
        Heading(sm, 400)
        outcome = sm.execute()

    sis = IntrospectionServer('ALPHEUS_MISSION_PLANNER', sm, '/SM_ROOT')
    sis.start()

if __name__ == '__main__':
    main()
