#!/usr/bin/env python
try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

import rospy
from video import video
import threading
import time
from alpheus_msgs.msg import hsv
import numpy as np


class hsvDynClient:
    def __init__(self, frameVideo, row, column, name):
        self.row = row
        self.column = column
        frame = Frame(frameVideo, bg='white')
        frame.grid(row=self.row, column=self.column, sticky=W, padx=15, pady=15)
        self.labelFrame = LabelFrame(frame, text=name, font="Helvetica 15 bold")
        self.v = IntVar()
        Radiobutton(self.labelFrame, text="Red",font="Helvetica 13", variable=self.v, value=1).grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Radiobutton(self.labelFrame, text="Green",font="Helvetica 13",variable=self.v, value=2).grid(row=0, column=1, sticky=W, padx=5, pady=5)
        Label(self.labelFrame, text="Hue Min", font="Helvetica 13").grid(row=2,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Saturation Min", font="Helvetica 13").grid(row=3,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Value Min", font="Helvetica 13").grid(row=4,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Hue Max", font="Times").grid(row=5,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Saturation Max", font="Helvetica 13").grid(row=6,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Value Max", font="Times").grid(row=7,sticky=W,padx=5,pady=5)
        self.hmin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.hmin.grid(row=2, column=1)
        self.smin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.smin.grid(row=3, column=1)
        self.vmin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.vmin.grid(row=4, column=1)
        self.hmax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.hmax.grid(row=5, column=1)
        self.smax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.smax.grid(row=6, column=1)
        self.vmax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL)
        self.vmax.grid(row=7, column=1)
        self.labelFrame.pack()
        
        self.hsvPublisher = rospy.Publisher("/hsv",hsv,queue_size=500)
        
        t = threading.Thread(target=self.hsvPub)
        t.start()

    def hsvPub(self):
        while True: # Replace with while Tkinter Loop is running
            hsvmsg = hsv()
            hsvmsg.color = np.uint8(self.v.get())
            hsvmsg.hmax = np.uint8(self.hmax.get())
            hsvmsg.smax = np.uint8(self.smax.get())
            hsvmsg.vmax = np.uint8(self.vmax.get())
            hsvmsg.hmin = np.uint8(self.hmin.get())
            hsvmsg.smin = np.uint8(self.smin.get())
            hsvmsg.vmin = np.uint8(self.vmin.get())

            self.hsvPublisher.publish(hsvmsg)
