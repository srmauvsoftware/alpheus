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
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from alpheus_msgs.msg import pressure

class pressureUI:
    def __init__(self, frameTele, root):
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

        '''
        self.f = Figure(figsize=(5,5), dpi=50)

        canvas = FigureCanvasTkAgg(self.f, groupOrientation)
        canvas.show()
        canvas.get_tk_widget().grid(row=2,column=2,sticky=W,padx=15,pady=15)
        self.t = 0
        self.a = self.f.add_subplot(111)
        self.a.set_ylim(0, 1000)
        self.line, = self.a.plot([],[], color = (0,0,1))
        root.after(1000)
        '''


    def pressure_cb(self, data):
        self.vX.set(str(data.pressure))

        #Convert Pressure To Depth and Display in Depth Field
        #self.vY.set(str(data.pressure))
'''
    def animateWrapper(self):
        animation.FuncAnimation(self.f, self.animate, np.arange(0,1000), interval=50, blit=False)

    def animate(self):
        self.a.set_xlim(self.t)
        self.line.set_xdata(self.t)
        print("Im here")
        self.line.set_ydata((int)(data.pressure))
        return self.line,
'''
