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
from alpheus_actions.msg import headingGoal, headingAction
import threading

class headingActionUI:
    def __init__(self, frameControl):
        f = Frame(frameControl, bg='white')
        f.grid(row=0, column=1, sticky=N, padx = 15, pady = 15)
        g = LabelFrame(f, text="Heading Action", font="Times")
        newDepthLabel = Label(g, text="Enter New Heading", font="Times")
        self.newDepthInput= Entry(g)
        newDepthButton = Button(g, text = "GO", font="Times", command = self.goDepth, width = 1)
        newDepthLabel.grid(row=1)
        self.newDepthInput.grid(row=1, column=2)
        newDepthButton.grid(row=2)
        g1 = LabelFrame(f, text="Status", font="Times")
        self.status = ""
        self.statusLabel = Label(g1, text=self.status, font="Times")
        self.statusLabel.grid(row=0)
        g.pack()
        g1.pack()


    def goDepth(self):
        t = threading.Thread(target=self.goDepthThreaded)
        t.start()

    def goDepthThreaded(self):
        client = actionlib.SimpleActionClient('headingServer', headingAction)
        self.status += "Connecting to HeadingServer \n"
        self.statusLabel.config(text=self.status)
        client.wait_for_server()
        self.status += "Connected to HeadingServer \n"
        self.statusLabel.config(text=self.status)
        goal = headingGoal(heading_setpoint=(float)(self.newDepthInput.get()))
        client.send_goal(goal)
        self.status += "Goal Sent. Waiting for Result... \n"
        self.statusLabel.config(text=self.status)
        client.wait_for_result()
        self.status += "Result : " + (str)(client.get_result()) + "\n" + "Finished"
        self.statusLabel.config(text=self.status)
