#! /usr/bin/env python
from __future__ import print_function
import rospy
import actionlib
import alpheus_actions.msg

def taskClient():
    client = actionlib.SimpleActionClient('taskServer', alpheus_actions.msg.taskAction)
    client.wait_for_Server()
    goal = alpheus_actions.msg.taskGoal(task_number = 1) # 0-path, 1-gate, 2-buoy
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('taskClient')
        result = taskClient()
        print(result)
    except rospy.ROSInterruptException:
        print("Program interrupted before completion", file=sys.stderr)        
