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

class angularVelocityUI:
    def __init__(self, frameTele):
        rospy.Subscriber('/imu/data', Imu, self.imu_callback)
        #Orientation
        frameOrientation = Frame(frameTele , bg='white')
        frameOrientation.grid(row=1, column=1, sticky=W, padx=15, pady=15)
        # grouping of widgets
        groupOrientation = LabelFrame(frameOrientation, text="Angular Velocity",font="Times")
        groupOrientation.pack()
	    # widget definitions
        lblX = Label(groupOrientation, text="X:",font="Times")
        lblY = Label(groupOrientation, text="Y:",font="Times")
        lblZ = Label(groupOrientation, text="Z:",font="Times")
	    # declare and initialize variables
        self.vX = StringVar()
        self.vX.set("X")
        self.vY = StringVar()
        self.vY.set("Y")
        self.vZ = StringVar()
        self.vZ.set("Z")
	    # associate variables with labels displaying data
        self.entXData = Entry(groupOrientation, textvariable=self.vX, background="blue",font="Times")
        self.entYData = Entry(groupOrientation, textvariable=self.vY, background="blue",font="Times")
        self.entZData = Entry(groupOrientation, textvariable=self.vZ, background="blue",font="Times")
	    # layout widgets within group
        lblX.grid(row=0,sticky=W,padx=5,pady=5)
        lblY.grid(row=1,sticky=W,padx=5,pady=5)
        lblZ.grid(row=2,sticky=W,padx=5,pady=5)
        self.entXData.grid(row=0,column=1)
        self.entYData.grid(row=1,column=1)
        self.entZData.grid(row=2,column=1)

    def imu_callback(self, data):
        self.vX.set(str(round(data.angular_velocity.x,1)))
        self.vY.set(str(round(data.angular_velocity.y,1)))
        self.vZ.set(str(round(data.angular_velocity.z,1)))
