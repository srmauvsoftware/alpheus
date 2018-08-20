#! /usr/bin/env python

import rospy
from __future__ import print_function

import actionlib
import sensor_msgs
import cv2
import darknet_ros_msgs

def checkForObjectsResultCB(goalState, result):
    print("Received Bounding Boxes")
    boundingBoxesResults_ = result.bounding_boxes

def sendImageToYolo(Image):
    
