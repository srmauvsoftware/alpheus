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
from dynamic_reconfigure.server import Server
from vision.cfg import hsvConfig

class Gate:
    def __init__(self):
        self.imageSub = rospy.Subscriber("/alpheus_cam/front/image_raw", Image, self.img_cb)
        srv = Server(hsvConfig, self.dyn_cb)
        self.bridge = CvBridge()
        self.offsetData = offsetData()
        self.imagePub = rospy.Publisher("/front/gate", Image , queue_size=2)
        self.offsetPub = rospy.Publisher("/offsetData", offsetData, queue_size=2)
        self.erosion = None
        self.dilation = None
        self.cameraX = 640 / 2
        self.cameraY = 320 / 2
        self.r_hmin = 0
        self.r_smin = 0
        self.r_vmin = 0
        self.r_hmax = 0
        self.r_smax = 0
        self.r_vmax = 0
        self.g_hmin = 0
        self.g_smin = 0
        self.g_vmin = 0
        self.g_hmax = 0
        self.g_smax = 0
        self.g_vmax = 0

    def dyn_cb(self, config, level):
        rospy.loginfo("Dynamic Reconfigure Started For HSV Values")
        rgb = config["rgb"]
        print(config)
        if(rgb == 1):
            self.r_hmin = config["h_min"]
            self.r_smin = config["s_min"]
            self.r_vmin = config["v_min"]
            self.r_hmax = config["h_max"]
            self.r_smax = config["s_max"]
            self.r_vmax = config["v_max"]

        if(rgb == 2):
            self.g_hmin = config["h_min"]
            self.g_smin = config["s_min"]
            self.g_vmin = config["v_min"]
            self.g_hmax = config["h_max"]
            self.g_smax = config["s_max"]
            self.g_vmax = config["v_max"]

        return config

    def filter_image(self, cv_image):
        channels = cv2.split(cv_image)
        channels[0] = cv2.equalizeHist(channels[0])
        channels[1] = cv2.equalizeHist(channels[1])
        return cv2.merge(channels, cv_image)

    def largestContour(self, contours):
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray = append(area)
        sorteddata = sorted(zip(areaArray, contours), key = lambda x: x[0], reverse=True)
        return sorteddata[0][1]

    def findOffsets(self, x, y):
        if( x < self.cameraX and y < self.cameraY ):
            offsetX = self.cameraX - x
            offsetY = self.cameraY - y
        elif( x > self.cameraX and y < self.cameraY ):
            offsetX = x - self.cameraX
            offsetY = self.cameraY - y
        elif( x < self.cameraX and y > self.cameraY):
            offsetX = self.cameraX - x
            offsetY = y - self.cameraY
        elif( x > self.cameraY and y > self.cameraY):
            offsetX = x - self.cameraX
            offsetY = y - self.cameraY
        return offsetX, offsetY

    def img_cb(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        lowerRed = np.array([ self.r_hmin, self.r_smin , self.r_vmin ])
        upperRed = np.array([ self.r_hmax, self.r_smax, self.r_vmax ])
        lowerGreen = np.array([ self.g_hmin, self.g_smin, self.g_vmin ])
        upperGreen = np.array([ self.g_hmax, self.g_smax, self.g_vmax ])

        hsvRed = cv2.cvtColor(self.filter_image(cv_image), cv2.COLOR_BGR2HSV)
        hsvGreen = cv2.cvtColor(self.filter_image(cv_image), cv2.COLOR_BGR2HSV)
        maskRed = cv2.inRange(hsvRed, lowerRed, upperRed)
        maskGreen = cv2.inRange(hsvGreen, lowerGreen, upperGreen)

        if(self.erosion and self.dilation):
            erodeKernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(self.erosion, self.erosion))
            dilateKernel = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=(self.dilation,self.dilation))
            cv2.erode(maskRed, erodeKernel, maskRed)
            cv2.erode(maskGreen, erodeKernel, maskGreen)
            cv2.dilate(maskRed, dilateKernel, maskRed)
            cv2.dilate(maskGreen, dilateKernel, maskGreen)

        contoursRed = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        contoursGreen = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        itr = -1
        a = 0
        self.offsetData.offsetX = 0
        self.offsetData.offsetY = 0
        if not contours:
            print("No Contours Found")
        else:
            pipeRed = self.largestContour(contoursRed)
            pipeGreen = self.largestContour(contoursGreen)
            Rx, Ry, Rh, Rw = cv2.boundingRect(pipeRed)
            Gx, Gy, Gh, Gw = cv2.boundingRect(pipeGreen)
            redCenter = ( Rx + (Rw / 2) , Ry + (Rh / 2) )
            greenCenter = ( Gx + (Gw / 2) , Gy + (Gh / 2) )
            cv2.circle(cv_image, redCenter, 3, (255,0,0), -1)
            cv2.rectangle(cv_image, (Rx, Ry), (Rx + Rw, Ry + Rh), (255, 0, 0), 2)
            cv2.circle(cv_image, greenCenter, 3, (0,255,0), -1)
            cv2.rectangle(cv_image, (Gx, Gy), (Gx + Gw, Gy + Gh), (0, 255, 0), 2)
            cv2.circle(cv_image, (cameraX, cameraY), 3, (255, 255, 255), -1)	#draw center
            cv2.line(cv_image, (Rx+(Rw/2), Ry+(Rh/2)),(cameraX, cameraY),(255, 0, 0),3)
            cv2.line(cv_image, (Gx+(Gw/2), Gy+(Gh/2)),(cameraX, cameraY),(0, 255, 0),3)

            gateCenter = ( (redCenter[0] + greenCenter[0]) / 2 , (redCenter[1] + redCenter[1]) / 2 )
            gateCenter = findOffsets(gateCenter)
            self.offsetData.offsetX = gateCenter[0]
            self.offsetData.offsetY = gateCenter[1]

            self.imagePub.publish(self.bridge.cv2_to_imgmsg(cv_image), "bgr8")
            self.offsetPub.publish(self.offsetData)

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
