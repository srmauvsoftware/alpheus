#!/usr/bin/env python
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage
from alpheus_msgs.msg import *
from cv_bridge import CvBridge, CvBridgeError
import rostopic

class Vision:
    def __init__(self):
        self.bridge = CvBridge()
        self.front_imagePub = rospy.Publisher("/front", CompressedImage, queue_size=2)
        self.bottom_imagePub = rospy.Publisher("/bottom", offsetData, queue_size=2)
        self.offsetPub = rospy.Publisher("/offsetData", offsetData, queue_size=2)



def main(args):
    rospy.init_node('FrontCamVision')
    ic = Gate()
    rate = rospy.Rate(1)
    try:
        rospy.spin()
        rate.sleep()
    except KeyboardInterrupt:
        print("Keyboard Interrupt : Shutting Down")

if __name__ == '__main__':
    main(sys.argv)
