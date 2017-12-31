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
from UIs.TelemetryUI.thrusterUI import thrusterUI
from UIs.TelemetryUI.orientationUI import orientationUI
from UIs.TelemetryUI.angularVelocityUI import angularVelocityUI
from UIs.TelemetryUI.linearAccelerationUI import linearAccelerationUI
from UIs.TelemetryUI.pidUI import pidUI
from UIs.TelemetryUI.pressureUI import pressureUI
from UIs.ControllerUI.depthActionUI import depthActionUI
from UIs.ControllerUI.headingActionUI import headingActionUI
from UIs.VisionUI.videoUI import videoUI

class gui:
    def __init__(self, master):
        master.title('AUV Telemetry')
        self.customFont = tkFont.Font(None, size=12)
        nb = ttk.Notebook(master)
        nb.grid(row=1, column=0,sticky='NESW')

        frameTele = ttk.Frame(nb)
        nb.add(frameTele,text="Telemetry")
        thrusterUI(frameTele)
        orientationUI(frameTele)
        angularVelocityUI(frameTele)
        linearAccelerationUI(frameTele)
        pidUI(frameTele)
        pressureUI(frameTele)

        frameControl = ttk.Frame(nb)
        nb.add(frameControl,text="Controller")
        depthActionUI(master, frameControl)
        headingActionUI(master, frameControl)

        frameVideo = ttk.Frame(nb)
        nb.add(frameVideo, text="Image Processing")
        videoUI(frameVideo)

        '''


        frameAtt1 = Frame(frameControl, bg='white')
        frameAtt1.grid(row=0, column=0,sticky=N,padx=15,pady=15)

        frameAtt2 = Frame(frameControl, bg='white')
        frameAtt2.grid(row=0, column=1,sticky=N,padx=15,pady=15)
        groupAtt2 = LabelFrame(frameAtt2, text="Goal", font=self.customFont)
        bstartgoal= Button(groupAtt2,text= "Start Goal",background='blue')
        bendgoal = Button(groupAtt2, text="End Goal",background='blue')

        bdisablepid = Button(groupAtt2, text="Disable Pid", background='blue')
        bstartgoal.grid(row=1,sticky=W,padx=5,pady=5)
        bendgoal.grid(row=2,sticky=W,padx=5,pady=5)
        bdisablepid.grid(row=3,sticky=W,padx=5,pady=5)
        groupAtt2.pack()

        frameAtt3 =Frame(frameControl,bg='white')
        frameAtt3.grid(row=0,column=2,sticky=N,padx=15,pady=15)
        groupAtt3 = LabelFrame(frameAtt3,text="action",font=self.customFont)
        bhover= Button(groupAtt3,text="Hover",background='blue')
        bsurface= Button(groupAtt3,text="Surface",background='blue')
        bhomebase=Button(groupAtt3,text="Home base",background='blue')
        bhover.grid(row=1,sticky=W,padx=5,pady=5)
        bsurface.grid(row=2,sticky=W,padx=5,pady=5)
        bhomebase.grid(row=3,sticky=W,padx=5,pady=5)
        groupAtt3.pack()

        frameAtt4= Frame(frameControl,bg='white')
        frameAtt4.grid(row=1,column=0,sticky=W,padx=15,pady=15)
        groupAtt4 = LabelFrame(frameAtt4,text="Navigation",font=self.customFont)
        lblxcoordinate = Label(groupAtt4,text="X-Coordinate:", font=self.customFont)
        lblycoordinate = Label(groupAtt4, text="Y-Coordinate:", font=self.customFont)
        xinput= Entry(groupAtt4)
        yinput= Entry(groupAtt4)
        go=Button(groupAtt4,text="Go",font=self.customFont)
        lblxcoordinate.grid(row=1)
        lblycoordinate.grid(row=2)
        go.grid(row=3)
        xinput.grid(row=1,column=2)
        yinput.grid(row=2,column=2)
        groupAtt4.pack()
        '''

if __name__ == '__main__':
    rospy.init_node('gui', anonymous=True)
    root = Tk()
    myGui = gui(root)
    root.mainloop()
