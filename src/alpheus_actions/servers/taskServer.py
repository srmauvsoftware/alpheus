#! /usr/bin/env python

'''
this will receive goal as the task number from taskClient present in
alpheus_actions/clients
it will check which task to execute. If(say)it needs to execute gate task, then
it will subscribe to yolo's 'bounding_boxes' topic to recieve the bounding box
coordinates it will then calculate the offsets and send the offsetY to depth
server and offsetX to heading server.
As of now there is also a DepthHeading state machine created which can also act
as a client to the depth and heading servers. It is not being used if this
approach is used.
'''

import rospy
import actionlib
import alpheus_actions.msg
from alpheus_msgs.msg import *

class taskAction(object):
    # create messages that are used to publish feedback/result
    _feedback = alpheus_actions.msg.taskFeedback()
    _result = alpheus_actions.msg.taskResult()

    def __init__(self, name):
        rospy.Subscriber("/bounding_boxes", BoundingBoxes, self.task_cb)
        self.offsetX = 0
        self.offsetY = 0
        self.ta = name
        self._ts = actionlib.SimpleActionServer(
            self._ta, \
            alpheus_actions.msg.taskAction, \
            execute_cb = self.taskCallback, \
            auto_start= False)
        self._ts.start()

    def taskCallback(self, data):
        publish_offsets(data.center_x, data.center_y)

        def taskCallback(self, goal):
            r = rospy.rate(10)
            success = True
            ot =


if __name__ == '__main__':
    rospy.init_node('taskServer')
    server = taskAction(rospy.get_name())
    rospy.spin()


class clients:


make 1 class and 2 objects. 1 object for each depth and heading
