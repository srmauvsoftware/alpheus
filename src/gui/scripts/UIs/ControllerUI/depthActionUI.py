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
import actionlib
from alpheus_actions.msg import depthGoal, depthAction
import threading

class depthActionUI:
    def __init__(self, frameControl):
        f = Frame(frameControl, bg='white')
        f.grid(row=0, column=0, sticky=N, padx = 15, pady = 15)
        g = LabelFrame(f, text="DEPTH ACTION", font="Helvetica 15 bold")
        newDepthLabel = Label(g, text="Enter New Depth", font="Helvetica 13")
        self.newDepthInput= Entry(g)
        newDepthButton = Button(g, text = "GO", font="Helvetica 12", command = self.goDepth, width = 1)
        newDepthLabel.grid(row=1)
        self.newDepthInput.grid(row=1, column=2)
        newDepthButton.grid(row=2)
        g1 = LabelFrame(f, text="STATUS", font="Helvetica 13 bold")
        self.status = ""
        self.statusLabel = Label(g1, text=self.status, font="Helvetica")
        self.statusLabel.grid(row=0)
        g.pack()
        g1.pack()

    def goDepth(self):
        t = threading.Thread(target=self.goDepthThreaded)
        t.start()


    def goDepthThreaded(self):
        client = actionlib.SimpleActionClient('depthServer', depthAction)
        self.status += "Connecting to DepthServer \n"
        self.statusLabel.config(text=self.status)
        client.wait_for_server()
        self.status += "Connected to DepthServer \n"
        self.statusLabel.config(text=self.status)
        goal = depthGoal(depth_setpoint=(float)(self.newDepthInput.get()))
        client.send_goal(goal)
        self.status += "Goal Sent. Waiting for Result... \n"
        self.statusLabel.config(text=self.status)
        client.wait_for_result()
        self.status += "Result : " + (str)(client.get_result()) + "\n" + "Finished"
        self.statusLabel.config(text=self.status)
