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
from alpheus_msgs.msg import pressure

class pressureUI:
    def __init__(self, frameTele):
        rospy.Subscriber('/pressure', pressure, self.pressure_cb)
        #Orientation
        frameOrientation = Frame(frameTele , bg='white')
        frameOrientation.grid(row=2, column=1, sticky=W, padx=15, pady=15)
        # grouping of widgets
        groupOrientation = LabelFrame(frameOrientation, text="Pressure",font="Times")
        groupOrientation.pack()
	    # widget definitions
        lblX = Label(groupOrientation, text="Pressure :",font="Times")
        lblY = Label(groupOrientation, text="Depth :",font="Times")
	    # declare and initialize variables
        self.vX = StringVar()
        self.vX.set("0")
        self.vY = StringVar()
        self.vY.set("0")
	    # associate variables with labels displaying data
        self.entXData = Entry(groupOrientation, textvariable=self.vX, background="blue",font="Times")
        self.entYData = Entry(groupOrientation, textvariable=self.vY, background="blue",font="Times")
	    # layout widgets within group
        lblX.grid(row=0,sticky=W,padx=5,pady=5)
        lblY.grid(row=1,sticky=W,padx=5,pady=5)
        self.entXData.grid(row=0,column=1)
        self.entYData.grid(row=1,column=1)

    def pressure_cb(self, data):
        self.vX.set(str(data.pressure))
        #Convert Pressure To Depth and Display in Depth Field
        #self.vY.set(str(data.pressure))
