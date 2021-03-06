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
from sensor_msgs.msg import Imu

class orientationUI:
    def __init__(self, frameTele):
        rospy.Subscriber('/imu/data', Imu, self.imu_callback)
        #Orientation
        frameOrientation = Frame(frameTele , bg='white')
        frameOrientation.grid(row=1, column=0,sticky=W,padx=15,pady=15)
        # grouping of widgets
        groupOrientation = LabelFrame(frameOrientation, text="ORIENTATION",font="Helvetica 15 bold")
        groupOrientation.pack()
	    # widget definitions
        lblX = Label(groupOrientation, text="Degree X:",font="Helvetica 13")
        lblY = Label(groupOrientation, text="Degree Y:",font="Helvetica 13")
        lblZ = Label(groupOrientation, text="Degree Z:",font="Helvetica 13")
        lblW = Label(groupOrientation, text="Degree W:",font="Helvetica 13")
	    # declare and initialize variables
        self.vX = StringVar()
        self.vX.set("X")
        self.vY = StringVar()
        self.vY.set("Y")
        self.vZ = StringVar()
        self.vZ.set("Z")
        self.vW = StringVar()
        self.vW.set("W")
	    # associate variables with labels displaying data
        self.entXData = Entry(groupOrientation, textvariable=self.vX, background="white",font="Helvetica")
        self.entYData = Entry(groupOrientation, textvariable=self.vY, background="white",font="Helvetica")
        self.entZData = Entry(groupOrientation, textvariable=self.vZ, background="white",font="Helvetica")
        self.entWData = Entry(groupOrientation, textvariable=self.vW, background="white",font="Helvetica")
	    # layout widgets within group
        lblX.grid(row=0,sticky=W,padx=5,pady=5)
        lblY.grid(row=1,sticky=W,padx=5,pady=5)
        lblZ.grid(row=2,sticky=W,padx=5,pady=5)
        lblW.grid(row=3,sticky=W,padx=5,pady=5)
        self.entXData.grid(row=0,column=1)
        self.entYData.grid(row=1,column=1)
        self.entZData.grid(row=2,column=1)
        self.entWData.grid(row=3,column=1)

    def imu_callback(self, data):
        self.vX.set(str(round(data.orientation.x,1)))
        self.vY.set(str(round(data.orientation.y,1)))
        self.vZ.set(str(round(data.orientation.z,1)))
        self.vW.set(str(round(data.orientation.w,1)))
