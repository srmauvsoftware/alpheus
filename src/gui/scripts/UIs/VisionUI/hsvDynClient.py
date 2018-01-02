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
import dynamic_reconfigure.client


class hsvDynClient:
    def __init__(self, frameVideo, row, column, name):
        self.row = row
        self.column = column
        rospy.wait_for_service("vision")
        self.client = dynamic_reconfigure.client.Client("vision", timeout=30, config_callback=self.callback)
        frame = Frame(frameVideo, bg='white')
        frame.grid(row=self.row, column=self.column, sticky=W, padx=15, pady=15)
        self.labelFrame = LabelFrame(frame, text=name, font="Times")
        self.v = IntVar()
        Radiobutton(self.labelFrame, text="Red", variable=self.v, value=1).grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Radiobutton(self.labelFrame, text="Green", variable=self.v, value=2).grid(row=0, column=1, sticky=W, padx=5, pady=5)
        Label(self.labelFrame, text="Hue Min", font="Times").grid(row=2,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Saturation Min", font="Times").grid(row=3,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Value Min", font="Times").grid(row=4,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Hue Max", font="Times").grid(row=5,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Saturation Max", font="Times").grid(row=6,sticky=W,padx=5,pady=5)
        Label(self.labelFrame, text="Value Max", font="Times").grid(row=7,sticky=W,padx=5,pady=5)
        self.hmin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=2, column=1)
        self.smin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=3, column=1)
        self.vmin = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=4, column=1)
        self.hmax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=5, column=1)
        self.smax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=6, column=1)
        self.vmax = Scale(self.labelFrame, from_=0, to=255, orient=HORIZONTAL).grid(row=7, column=1)
        self.labelFrame.pack()
        client.update_configuration({
            "rgb": self.v.get(),
            "hmin": self.hmin.get(),
            "smin": self.smin.get(),
            "vmin": self.vmin.get(),
            "hmax": self.hmax.get(),
            "smax": self.smax.get(),
            "vmax": self.vmax.get()
        })

    def callback(config):
        rospy.loginfo("Config Updated")
