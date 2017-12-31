#!/usr/bin/env python
try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

import PIL.Image
import PIL.ImageTk
import threading
import datetime
import imutils
import cv2
import os
import roslib
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
'''
To Do -
* Implement Threading
* Path For Saving
'''
class videoUI:
    def __init__(self, frameVideo):
        rospy.Subscriber('/usb_cam/image_raw', Image, self.image_cb)
        self.bridge = CvBridge()
        frame = Frame(frameVideo, bg='white')
        frame.grid(row=1, column=1, sticky=W, padx=15, pady=15)
        self.labelFrame = LabelFrame(frame, text="Front Camera", font="Times")
        self.panel = None
        snapButton = Button(self.labelFrame, text="Snapshot!", command = self.takeSnapshot).grid(column=2)
        self.labelFrame.pack()

    def image_cb(self, data):
        try:
            image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image_cv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = imutils.resize(self.image_cv, width=300)
            image = PIL.Image.fromarray(image)
            image = PIL.ImageTk.PhotoImage(image)
            if self.panel is None:
                self.panel = Label(self.labelFrame, image=image)
                self.panel.image = image
                self.panel.grid(row=1, column=2, sticky=W, padx=5, pady=5)
            else:
                self.panel.configure(image=image)
                self.panel.image = image

        except CvBridgeError as e:
            print(e)

    def takeSnapshot(self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        cv2.imwrite(filename, self.image_cv)
        print("Image Saved")
