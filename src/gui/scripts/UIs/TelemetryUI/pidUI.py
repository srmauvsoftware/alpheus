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
from alpheus_msgs.msg import pressurePID
from alpheus_msgs.msg import headingPID
import threading

class pidUI:
    def __init__(self, container, row, col, loc=None):

        if loc == "frameTele":
            rospy.Subscriber('/pressurePIDdata', pressurePID, self.pressure_cb)
            rospy.Subscriber('/headingPIDdata', headingPID, self.heading_cb)

        #Orientation
        frameOrientation = Frame(container , bg='white')
        frameOrientation.grid(row=row, column=col, sticky=W, padx=15, pady=15)
        # grouping of widgets
        groupOrientation = LabelFrame(frameOrientation, text="PID",font="Helvetica 15 bold")
        groupOrientation.pack()
	    # widget definitions
        lblX = Label(groupOrientation, text="pKp:",font="Helvetica 13")
        lblY = Label(groupOrientation, text="pKi:",font="Helvetica 13")
        lblZ = Label(groupOrientation, text="pKd:",font="Helvetica 13")
        lblhX = Label(groupOrientation, text="hKp:",font="Helvetica 13")
        lblhY = Label(groupOrientation, text="hKi:",font="Helvetica 13")
        lblhZ = Label(groupOrientation, text="hKd:",font="Helvetica 13")

	    # declare and initialize variables
        self.vX = StringVar()
        self.vX.set("0")
        self.vY = StringVar()
        self.vY.set("0")
        self.vZ = StringVar()
        self.vZ.set("0")
        self.vhX = StringVar()
        self.vhX.set("0")
        self.vhY = StringVar()
        self.vhY.set("0")
        self.vhZ = StringVar()
        self.vhZ.set("0")
	    # associate variables with labels displaying data
        self.entXData = Entry(groupOrientation, textvariable=self.vX, background="white",font="Helvetica")
        self.entYData = Entry(groupOrientation, textvariable=self.vY, background="white",font="Helvetica")
        self.entZData = Entry(groupOrientation, textvariable=self.vZ, background="white",font="Helvetica")
        self.enthXData = Entry(groupOrientation, textvariable=self.vhX, background="white",font="Helvetica")
        self.enthYData = Entry(groupOrientation, textvariable=self.vhY, background="white",font="Helvetica")
        self.enthZData = Entry(groupOrientation, textvariable=self.vhZ, background="white",font="Helvetica")
	    # layout widgets within group
        lblX.grid(row=0,sticky=W,padx=5,pady=5)
        lblY.grid(row=1,sticky=W,padx=5,pady=5)
        lblZ.grid(row=2,sticky=W,padx=5,pady=5)
        self.entXData.grid(row=0,column=1)
        self.entYData.grid(row=1,column=1)
        self.entZData.grid(row=2,column=1)
        lblhX.grid(row=3,sticky=W,padx=5,pady=5)
        lblhY.grid(row=4,sticky=W,padx=5,pady=5)
        lblhZ.grid(row=5,sticky=W,padx=5,pady=5)
        self.enthXData.grid(row=3,column=1)
        self.enthYData.grid(row=4,column=1)
        self.enthZData.grid(row=5,column=1)

        if container == "frameControl":
            snapButton = Button(groupOrientation, text="Update PID", command = self.publishPID).grid(row=6,column=1)

    def pressure_cb(self, data):
        self.vX.set(str(data.pKp))
        self.vY.set(str(data.pKi))
        self.vZ.set(str(data.pKd))

    def heading_cb(self, data):
        self.vhX.set(str(data.hKp))
        self.vhY.set(str(data.hKi))
        self.vhZ.set(str(data.hKd))

    def publishPID(self):
        self.Ppublisher = rospy.Publisher("/pressurePIDdata", pressurePID, queue_size=2)
        self.Hpublisher = rospy.Publisher("/headingPIDdata", headingPID, queue_size=2)

        pmsg = pressurePID()
        pmsg.pKp = float(self.vX.get())
        pmsg.pKi = float(self.vY.get())
        pmsg.pKd = float(self.vZ.get())

        hmsg = headingPID()
        hmsg.hKp = float(self.vhX.get())
        hmsg.hKi = float(self.vhY.get())
        hmsg.hKd = float(self.vhZ.get())

        self.Ppublisher.publish(pmsg)
        self.Hpublisher.publish(hmsg)
