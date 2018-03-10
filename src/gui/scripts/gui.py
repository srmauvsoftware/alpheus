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
from UIs.VisionUI.frontCamUI import frontCamUI
from UIs.VisionUI.bottomCamUI import bottomCamUI

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
        pidUI(frameTele,2,1, loc="frameTele")
        pidUI(frameTele,2,2, loc="frameTele")
        pressureUI(frameTele, master)

        frameControl = ttk.Frame(nb)
        nb.add(frameControl,text="Controller")
        depthActionUI(frameControl)
        pidUI(frameControl,1,0, loc="frameControl")
        headingActionUI(frameControl)

        frameVideoFront = ttk.Frame(nb)
        nb.add(frameVideoFront, text="Front Camera")
        frontCamUI(frameVideoFront)

        frameVideoBottom = ttk.Frame(nb)
        nb.add(frameVideoBottom, text="Bottom Camera")
        bottomCamUI(frameVideoBottom)

if __name__ == '__main__':
    rospy.init_node('gui', anonymous=True)
    root = Tk()
    myGui = gui(root)
    root.mainloop()
