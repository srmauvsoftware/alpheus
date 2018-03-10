#!/usr/bin/env python
try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

from alpheus_msgs.msg import thruster
import rospy

class thrusterUI:
    def __init__(self, frameTele):
        rospy.Subscriber('/thruster', thruster, self.thruster_callback)
        frameThrusterSpeed = Frame(frameTele , bg='white')
        frameThrusterSpeed.grid(row=2, column=0, rowspan=2,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupThrusterSpeed = LabelFrame(frameThrusterSpeed, text="Thruster PWM" ,font="Helvetica 15 bold")
        groupThrusterSpeed.pack()
	    # widget definitions
        lblThrusterSpeed1 = Label(groupThrusterSpeed, text="Forward 1:",font="Helvetica 13")
        lblThrusterSpeed2 = Label(groupThrusterSpeed, text="Forward 2:",font="Helvetica 13")
        lblThrusterSpeed3 = Label(groupThrusterSpeed, text="Depth 1",font="Helvetica 13")
        lblThrusterSpeed4 = Label(groupThrusterSpeed, text="Depth 2",font="Helvetica 13")
        lblThrusterSpeed5 = Label(groupThrusterSpeed, text="Depth 3",font="Helvetica 13")
        lblThrusterSpeed6 = Label(groupThrusterSpeed, text="Depth 4",font="Helvetica 13")
        lblThrusterSpeed7 = Label(groupThrusterSpeed, text="Direction 1",font="Helvetica 13")
        lblThrusterSpeed8 = Label(groupThrusterSpeed, text="Direction 2",font="Helvetica 13")
	    # declare and initialize variables

        self.vThrusterSpeed1 = StringVar()
        self.vThrusterSpeed1.set("Forward 1")
        self.vThrusterSpeed2 = StringVar()
        self.vThrusterSpeed2.set("Forward 2")
        self.vThrusterSpeed3 = StringVar()
        self.vThrusterSpeed3.set("Up 1")
        self.vThrusterSpeed4 = StringVar()
        self.vThrusterSpeed4.set("Up 2")
        self.vThrusterSpeed5 = StringVar()
        self.vThrusterSpeed5.set("Up 3")
        self.vThrusterSpeed6 = StringVar()
        self.vThrusterSpeed6.set("Up 4")
        self.vThrusterSpeed7 = StringVar()
        self.vThrusterSpeed7.set("Direction 1")
        self.vThrusterSpeed8 = StringVar()
        self.vThrusterSpeed8.set("Direction 2")

	    # associate variables with labels displaying data
        self.entThrusterSpeed1Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed1, background="white",font="Helvetica")
        self.entThrusterSpeed2Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed2, background="white",font="Helvetica")
        self.entThrusterSpeed3Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed3, background="white",font="Helvetica")
        self.entThrusterSpeed4Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed4, background="white",font="Helvetica")
        self.entThrusterSpeed5Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed5, background="white",font="Helvetica")
        self.entThrusterSpeed6Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed6, background="white",font="Helvetica")
        self.entThrusterSpeed7Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed7, background="white",font="Helvetica")
        self.entThrusterSpeed8Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed8, background="white",font="Helvetica")
	    # layout widgets within group
        lblThrusterSpeed1.grid(row=0,sticky=W,padx=5,pady=5)
        lblThrusterSpeed2.grid(row=1,sticky=W,padx=5,pady=5)
        lblThrusterSpeed3.grid(row=2,sticky=W,padx=5,pady=5)
        lblThrusterSpeed4.grid(row=3,sticky=W,padx=5,pady=5)
        lblThrusterSpeed5.grid(row=4,sticky=W,padx=5,pady=5)
        lblThrusterSpeed6.grid(row=5,sticky=W,padx=5,pady=5)
        lblThrusterSpeed7.grid(row=6,sticky=W,padx=5,pady=5)
        lblThrusterSpeed8.grid(row=7,sticky=W,padx=5,pady=5)
        self.entThrusterSpeed1Data.grid(row=0,column=1)
        self.entThrusterSpeed2Data.grid(row=1,column=1)
        self.entThrusterSpeed3Data.grid(row=2,column=1)
        self.entThrusterSpeed4Data.grid(row=3,column=1)
        self.entThrusterSpeed5Data.grid(row=4,column=1)
        self.entThrusterSpeed6Data.grid(row=5,column=1)
        self.entThrusterSpeed7Data.grid(row=6,column=1)
        self.entThrusterSpeed8Data.grid(row=7,column=1)


    def thruster_callback(self, thruster):
        self.vThrusterSpeed1.set(str(round(thruster.speedfwd1,2)))
        self.vThrusterSpeed2.set(str(round(thruster.speedfwd2,2)))
        self.vThrusterSpeed3.set(str(round(thruster.speedup1,2)))
        self.vThrusterSpeed4.set(str(round(thruster.speedup2,2)))
        self.vThrusterSpeed5.set(str(round(thruster.speedup3,2)))
        self.vThrusterSpeed6.set(str(round(thruster.speedup4,2)))
        self.vThrusterSpeed7.set(str(round(thruster.speeddir1,2)))
        self.vThrusterSpeed8.set(str(round(thruster.speeddir2,2)))
