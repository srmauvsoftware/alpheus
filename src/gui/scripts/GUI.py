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
from std_msgs.msg import String
from beginner_tutorials.msg import *


class ListenGui:

    def __init__(self,master):

        # window title, size
        master.title('AUV Telemetry')
        self.customFont = tkFont.Font(None, size=12)

	nb = ttk.Notebook(master)
	nb.grid(row=1, column=0,sticky='NESW')

        frameTele = ttk.Frame(nb)
	nb.add(frameTele,text="Telemetry")
	frameControl = ttk.Frame(nb)
	nb.add(frameControl,text="Controller")

        #  Position
        # frame container
        framePos = Frame(frameTele , bg='cyan')
        framePos.grid(row=0, column=0,sticky=W,padx=15,pady=15)
        # grouping of widgets
        groupPos = LabelFrame(framePos, text="Position",font=self.customFont)
        groupPos.pack()
        # widget definitions
        lblPosX = Label(groupPos, text="X:", font=self.customFont)
        lblPosY = Label(groupPos, text="Y:",font=self.customFont)
        # declare and initialize variables
        self.vPosX = StringVar()
        self.vPosX.set("posX-data")
        self.vPosY = StringVar()
        self.vPosY.set("posY-data")
        # associate variables with labels displaying data
        self.entPosDataX = Entry(groupPos, textvariable=self.vPosX, background="pink",font=self.customFont)
        self.entPosDataY = Entry(groupPos, textvariable=self.vPosY, background="pink",font=self.customFont)
        # layout widgets within group
        lblPosX.grid(row=0,sticky=W,padx=5,pady=5)
        lblPosY.grid(row=1,sticky=W,padx=5,pady=5)
        self.entPosDataX.grid(row=0,column=1)
        self.entPosDataY.grid(row=1,column=1)

        #Relative Position
        # frame container
        frameRelPos = Frame(frameTele , bg='cyan')
        frameRelPos.grid(row=0, column=1,sticky=W,padx=15,pady=15)
	    # grouping of widgets
        groupRelPos = LabelFrame(frameRelPos, text="Relative Position",font=self.customFont)
        groupRelPos.pack()
	    # widget definitions
        lblRelPosX = Label(groupRelPos, text="X:",font=self.customFont)
        lblRelPosY = Label(groupRelPos, text="Y:",font=self.customFont)
        lblRelPosZ = Label(groupRelPos, text="Z:",font=self.customFont)
	    # declare and initialize variables
        self.vRelPosX = StringVar()
        self.vRelPosX.set("relPosX-data")
        self.vRelPosY = StringVar()
        self.vRelPosY.set("relPosY-data")
        self.vRelPosZ = StringVar()
        self.vRelPosZ.set("relPosZ-data")
	    # associate variables with labels displaying data
        self.entRelPosDataX = Entry(groupRelPos, textvariable=self.vRelPosX, background="pink",font=self.customFont)
        self.entRelPosDataY = Entry(groupRelPos, textvariable=self.vRelPosY, background="pink",font=self.customFont)
        self.entRelPosDataZ = Entry(groupRelPos, textvariable=self.vRelPosZ, background="pink",font=self.customFont)
	    # layout widgets within group
        lblRelPosX.grid(row=0,sticky=W,padx=5,pady=5)
        lblRelPosY.grid(row=1,sticky=W,padx=5,pady=5)
        lblRelPosZ.grid(row=2,sticky=W,padx=5,pady=5)
        self.entRelPosDataX.grid(row=0,column=1)
        self.entRelPosDataY.grid(row=1,column=1)
        self.entRelPosDataZ.grid(row=2,column=1)

        # Velocity
        # frame container
        frameVel = Frame(frameTele , bg='cyan')
        frameVel.grid(row=0, column=2,sticky=W,padx=15,pady=15)
        # grouping of widgets
        groupVel = LabelFrame(frameVel, text="Velocity",font=self.customFont)
        groupVel.pack()
	    # widget definitions
        lblVelX = Label(groupVel, text="X:",font=self.customFont)
        lblVelY = Label(groupVel, text="Y:",font=self.customFont)
        lblVelZ = Label(groupVel, text="Z:",font=self.customFont)
	    # declare and initialize variables
        self.vVelX = StringVar()
        self.vVelX.set("velX-data")
        self.vVelY = StringVar()
        self.vVelY.set("velY-data")
        self.vVelZ = StringVar()
        self.vVelZ.set("velZ-data")
	    # associate variables with labels displaying data
        self.entVelDataX = Entry(groupVel, textvariable=self.vVelX, background="pink",font=self.customFont)
        self.entVelDataY = Entry(groupVel, textvariable=self.vVelY, background="pink",font=self.customFont)
        self.entVelDataZ = Entry(groupVel, textvariable=self.vVelZ, background="pink",font=self.customFont)
	    # layout widgets within group
        lblVelX.grid(row=0,sticky=W,padx=5,pady=5)
        lblVelY.grid(row=1,sticky=W,padx=5,pady=5)
        lblVelZ.grid(row=2,sticky=W,padx=5,pady=5)
        self.entVelDataX.grid(row=0,column=1)
        self.entVelDataY.grid(row=1,column=1)
        self.entVelDataZ.grid(row=2,column=1)

        # Attitude-2
        # frame container
        frameAtt2 = Frame(frameTele , bg='white')
        frameAtt2.grid(row=1, column=0,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupAtt2 = LabelFrame(frameAtt2, text="Attitude",font=self.customFont)
        groupAtt2.pack()
	    # widget definitions
        lblDepth = Label(groupAtt2, text="Depth:",font=self.customFont)
        lblPressure = Label(groupAtt2, text="Pressure:",font=self.customFont)
        lblAltitude = Label(groupAtt2, text="Altitude:",font=self.customFont)
	    # declare and initialize variables
        self.vDepth = StringVar()
        self.vDepth.set("Depth-data")
        self.vPressure = StringVar()
        self.vPressure.set("Pressure-data")
        self.vAltitude = StringVar()
        self.vAltitude.set("Altitude-data")
	    # associate variables with labels displaying data
        self.entDepthData = Entry(groupAtt2, textvariable=self.vDepth, background="pink",font=self.customFont)
        self.entPressureData = Entry(groupAtt2, textvariable=self.vPressure, background="pink",font=self.customFont)
        self.entAltitudeData = Entry(groupAtt2, textvariable=self.vAltitude, background="pink",font=self.customFont)
	    # layout widgets within group
        lblDepth.grid(row=0,sticky=W,padx=5,pady=5)
        lblPressure.grid(row=1,sticky=W,padx=5,pady=5)
        lblAltitude.grid(row=2,sticky=W,padx=5,pady=5)
        self.entDepthData.grid(row=0,column=1)
        self.entPressureData.grid(row=1,column=1)
        self.entAltitudeData.grid(row=2,column=1)

        #Attitude-3
        # frame container
        frameAtt3 = Frame(frameTele , bg='white')
        frameAtt3.grid(row=1, column=1,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupAtt3 = LabelFrame(frameAtt3, text="Orientation",font=self.customFont)
        groupAtt3.pack()
	    # widget definitions
        lblYaw = Label(groupAtt3, text="Yaw:",font=self.customFont)
        lblPitch = Label(groupAtt3, text="Pitch:",font=self.customFont)
        lblRoll = Label(groupAtt3, text="Roll:",font=self.customFont)
	    # declare and initialize variables
        self.vYaw = StringVar()
        self.vYaw.set("Yaw-data")
        self.vPitch = StringVar()
        self.vPitch.set("Pitch-data")
        self.vRoll = StringVar()
        self.vRoll.set("Roll-data")
	    # associate variables with labels displaying data
        self.entYawData = Entry(groupAtt3, textvariable=self.vYaw, background="pink",font=self.customFont)
        self.entPitchData = Entry(groupAtt3, textvariable=self.vPitch, background="pink",font=self.customFont)
        self.entRollData = Entry(groupAtt3, textvariable=self.vRoll, background="pink",font=self.customFont)
	    # layout widgets within group
        lblYaw.grid(row=0,sticky=W,padx=5,pady=5)
        lblPitch.grid(row=1,sticky=W,padx=5,pady=5)
        lblRoll.grid(row=2,sticky=W,padx=5,pady=5)
        self.entYawData.grid(row=0,column=1)
        self.entPitchData.grid(row=1,column=1)
        self.entRollData.grid(row=2,column=1)


        #Battery
        # frame container
        frameBatt = Frame(frameTele , bg='white')
        frameBatt.grid(row=1, column=2,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupBatt = LabelFrame(frameBatt, text="Battery",font=self.customFont)
        groupBatt.pack()
	    # widget definitions
        lblVolt = Label(groupBatt, text="Volt:",font=self.customFont)
        lblCurrent = Label(groupBatt, text="Current:",font=self.customFont)
        lblPercentUsed = Label(groupBatt, text="PercentUsed:",font=self.customFont)
	    # declare and initialize variables
        self.vVolt = StringVar()
        self.vVolt.set("Volt-data")
        self.vCurrent = StringVar()
        self.vCurrent.set("Current-data")
        self.vPercentUsed = StringVar()
        self.vPercentUsed.set("PercentUsed-data")
	    # associate variables with labels displaying data
        self.entVoltData = Entry(groupBatt, textvariable=self.vVolt, background="pink",font=self.customFont)
        self.entCurrentData = Entry(groupBatt, textvariable=self.vCurrent, background="pink",font=self.customFont)
        self.entPercentUsedData = Entry(groupBatt, textvariable=self.vPercentUsed, background="pink",font=self.customFont)
	    # layout widgets within group
        lblVolt.grid(row=0,sticky=W,padx=5,pady=5)
        lblCurrent.grid(row=1,sticky=W,padx=5,pady=5)
        lblPercentUsed.grid(row=2,sticky=W,padx=5,pady=5)
        self.entVoltData.grid(row=0,column=1)
        self.entCurrentData.grid(row=1,column=1)
        self.entPercentUsedData.grid(row=2,column=1)


        # Temperature
        # frame container
        frameTemp = Frame(frameTele , bg='white')
        frameTemp.grid(row=2, column=0,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupTemp = LabelFrame(frameTemp, text="Temperature",font=self.customFont)
        groupTemp.pack()
	    # widget definitions
        lblTemp = Label(groupTemp, text="Temp:",font=self.customFont)
        lblCPUTemp = Label(groupTemp, text="CPUTemp:",font=self.customFont)
        lblHumidity = Label(groupTemp, text="Humidity:",font=self.customFont)
	    # declare and initialize variables
        self.vTemp = StringVar()
        self.vTemp.set("Temp-data")
        self.vCPUTemp = StringVar()
        self.vCPUTemp.set("CPUTemp-data")
        self.vHumidity = StringVar()
        self.vHumidity.set("Humidity-data")
	    # associate variables with labels displaying data
        self.entTempData = Entry(groupTemp, textvariable=self.vTemp, background="pink",font=self.customFont)
        self.entCPUTempData = Entry(groupTemp, textvariable=self.vCPUTemp, background="pink",font=self.customFont)
        self.entHumidityData = Entry(groupTemp, textvariable=self.vHumidity, background="pink",font=self.customFont)
	    # layout widgets within group
        lblTemp.grid(row=0,sticky=W,padx=5,pady=5)
        lblCPUTemp.grid(row=1,sticky=W,padx=5,pady=5)
        lblHumidity.grid(row=2,sticky=W,padx=5,pady=5)
        self.entTempData.grid(row=0,column=1)
        self.entCPUTempData.grid(row=1,column=1)
        self.entHumidityData.grid(row=2,column=1)


        #Hull Status
        # frame container
        frameLeak = Frame(frameTele , bg='white')
        frameLeak.grid(row=2, column=1,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupLeak = LabelFrame(frameLeak, text="Hull Status",font=self.customFont)
        groupLeak.pack()
	    # widget definitions
        lblLeak1 = Label(groupLeak, text="Leak 1:",font=self.customFont)
        lblLeak2 = Label(groupLeak, text="Leak 2:",font=self.customFont)
        lblLeak3 = Label(groupLeak, text="Leak 3:",font=self.customFont)
	    # declare and initialize variables
        self.vLeak1 = StringVar()
        self.vLeak1.set("Leak-1-data")
        self.vLeak2 = StringVar()
        self.vLeak2.set("Leak-2-data")
        self.vLeak3 = StringVar()
        self.vLeak3.set("Leak-3-data")

	    # associate variables with labels displaying data
        self.entLeak1Data = Entry(groupLeak, textvariable=self.vLeak1, background="pink",font=self.customFont)
        self.entLeak2Data = Entry(groupLeak, textvariable=self.vLeak2, background="pink",font=self.customFont)
        self.entLeak3Data = Entry(groupLeak, textvariable=self.vLeak3, background="pink",font=self.customFont)
	    # layout widgets within group
        lblLeak1.grid(row=0,sticky=W,padx=5,pady=5)
        lblLeak2.grid(row=1,sticky=W,padx=5,pady=5)
        lblLeak3.grid(row=2,sticky=W,padx=5,pady=5)
        self.entLeak1Data.grid(row=0,column=1)
        self.entLeak2Data.grid(row=1,column=1)
        self.entLeak3Data.grid(row=2,column=1)



        #Goal Definition
        # frame container
        frameGoal = Frame(frameTele , bg='white')
        frameGoal.grid(row=3, column=0,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupGoal = LabelFrame(frameGoal, text="Goal Status",font=self.customFont)
        groupGoal.pack()
	    # widget definitions
        lblHeading = Label(groupGoal, text="Heading:",font=self.customFont)
        lblForward = Label(groupGoal, text="Forward:",font=self.customFont)
        lblSideMove = Label(groupGoal, text="Side Move:",font=self.customFont)
        lblGoalDepth = Label(groupGoal, text="Depth:",font=self.customFont)
        lblGoalID = Label(groupGoal, text="Goal ID:",font=self.customFont)
	    # declare and initialize variables
        self.vHeading = StringVar()
        self.vHeading.set("heading-data")
        self.vForward = StringVar()
        self.vForward.set("fwd-data")
        self.vSideMove = StringVar()
        self.vSideMove.set("sm-data")
        self.vGoalDepth = StringVar()
        self.vGoalDepth.set("goal-depth-data")
        self.vGoalID = StringVar()
        self.vGoalID.set("goal-id-data")
	    # associate variables with labels displaying data
        self.entHeadingData = Entry(groupGoal, textvariable=self.vHeading, background="pink",font=self.customFont)
        self.entForwardData = Entry(groupGoal, textvariable=self.vForward, background="pink",font=self.customFont)
        self.entSideMoveData = Entry(groupGoal, textvariable=self.vSideMove, background="pink",font=self.customFont)
        self.entGoalDepthData = Entry(groupGoal, textvariable=self.vGoalDepth, background="pink",font=self.customFont)
        self.entGoalIDData = Entry(groupGoal, textvariable=self.vGoalID, background="pink",font=self.customFont)
	    # layout widgets within group
        lblHeading.grid(row=0,sticky=W,padx=5,pady=5)
        lblForward.grid(row=1,sticky=W,padx=5,pady=5)
        lblSideMove.grid(row=2,sticky=W,padx=5,pady=5)
        lblGoalDepth.grid(row=3,sticky=W,padx=5,pady=5)
        lblGoalID.grid(row=4,sticky=W,padx=5,pady=5)
        self.entHeadingData.grid(row=0,column=1)
        self.entForwardData.grid(row=1,column=1)
        self.entSideMoveData.grid(row=2,column=1)
        self.entGoalDepthData.grid(row=3,column=1)
        self.entGoalIDData.grid(row=4,column=1)


        #Goal Error
        # frame container
        frameGoalErr = Frame(frameTele , bg='white')
        frameGoalErr.grid(row=3, column=1,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupGoalErr = LabelFrame(frameGoalErr, text="GoalErr Status",font=self.customFont)
        groupGoalErr.pack()
	    # widget definitions
        lblHeadingErr = Label(groupGoalErr, text="HeadingErr:",font=self.customFont)
        lblForwardErr = Label(groupGoalErr, text="ForwardErr:",font=self.customFont)
        lblSideMoveErr = Label(groupGoalErr, text="Side Move:",font=self.customFont)
        lblGoalDepthErr = Label(groupGoalErr, text="Depth:",font=self.customFont)
        lblGoalStatus = Label(groupGoalErr, text="Goal ID:",font=self.customFont)
	    # declare and initialize variables
        self.vHeadingErr = StringVar()
        self.vHeadingErr.set("HeadingErr-data")
        self.vForwardErr = StringVar()
        self.vForwardErr.set("fwd-data")
        self.vSideMoveErr = StringVar()
        self.vSideMoveErr.set("sm-data")
        self.vGoalDepthErr = StringVar()
        self.vGoalDepthErr.set("goal-depth-data")
        self.vGoalStatus = StringVar()
        self.vGoalStatus.set("goal-id-data")
	    # associate variables with labels displaying data
        self.entHeadingErrData = Entry(groupGoalErr, textvariable=self.vHeadingErr, background="pink",font=self.customFont)
        self.entForwardErrData = Entry(groupGoalErr, textvariable=self.vForwardErr, background="pink",font=self.customFont)
        self.entSideMoveErrData = Entry(groupGoalErr, textvariable=self.vSideMoveErr, background="pink",font=self.customFont)
        self.entGoalDepthErrData = Entry(groupGoalErr, textvariable=self.vGoalDepthErr, background="pink",font=self.customFont)
        self.entGoalStatusData = Entry(groupGoalErr, textvariable=self.vGoalStatus, background="pink",font=self.customFont)
	    # layout widgets within group
        lblHeadingErr.grid(row=0,sticky=W,padx=5,pady=5)
        lblForwardErr.grid(row=1,sticky=W,padx=5,pady=5)
        lblSideMoveErr.grid(row=2,sticky=W,padx=5,pady=5)
        lblGoalDepthErr.grid(row=3,sticky=W,padx=5,pady=5)
        lblGoalStatus.grid(row=4,sticky=W,padx=5,pady=5)
        self.entHeadingErrData.grid(row=0,column=1)
        self.entForwardErrData.grid(row=1,column=1)
        self.entSideMoveErrData.grid(row=2,column=1)
        self.entGoalDepthErrData.grid(row=3,column=1)
        self.entGoalStatusData.grid(row=4,column=1)



        #Thruster Speed
        # frame container
        frameThrusterSpeed = Frame(frameTele , bg='white')
        frameThrusterSpeed.grid(row=2, column=2, rowspan=2,sticky=W,padx=15,pady=15) # columnspan?
        # grouping of widgets
        groupThrusterSpeed = LabelFrame(frameThrusterSpeed, text="ThrusterSpeed Status",font=self.customFont)
        groupThrusterSpeed.pack()
	    # widget definitions
        lblThrusterSpeed1 = Label(groupThrusterSpeed, text="ThrusterSpeed1:",font=self.customFont)
        lblThrusterSpeed2 = Label(groupThrusterSpeed, text="ThrusterSpeed2:",font=self.customFont)
        lblThrusterSpeed3 = Label(groupThrusterSpeed, text="ThrusterSpeed3:",font=self.customFont)
        lblThrusterSpeed4 = Label(groupThrusterSpeed, text="ThrusterSpeed4:",font=self.customFont)
        lblThrusterSpeed5 = Label(groupThrusterSpeed, text="ThrusterSpeed5:",font=self.customFont)
        lblThrusterSpeed6 = Label(groupThrusterSpeed, text="ThrusterSpeed6:",font=self.customFont)
        lblThrusterSpeed7 = Label(groupThrusterSpeed, text="ThrusterSpeed7:",font=self.customFont)
        lblThrusterSpeed8 = Label(groupThrusterSpeed, text="ThrusterSpeed8:",font=self.customFont)
	    # declare and initialize variables
        self.vThrusterSpeed1 = StringVar()
        self.vThrusterSpeed1.set("ThrusterSpeed1-data")
        self.vThrusterSpeed2 = StringVar()
        self.vThrusterSpeed2.set("fwd-data")
        self.vThrusterSpeed3 = StringVar()
        self.vThrusterSpeed3.set("sm-data")
        self.vThrusterSpeed4 = StringVar()
        self.vThrusterSpeed4.set("goal-depth-data")
        self.vThrusterSpeed5 = StringVar()
        self.vThrusterSpeed5.set("goal-id-data")
        self.vThrusterSpeed6 = StringVar()
        self.vThrusterSpeed6.set("ThrusterSpeed6-data")
        self.vThrusterSpeed7 = StringVar()
        self.vThrusterSpeed7.set("fwd-data")
        self.vThrusterSpeed8 = StringVar()
        self.vThrusterSpeed8.set("sm-data")
	    # associate variables with labels displaying data
        self.entThrusterSpeed1Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed1, background="pink",font=self.customFont)
        self.entThrusterSpeed2Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed2, background="pink",font=self.customFont)
        self.entThrusterSpeed3Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed3, background="pink",font=self.customFont)
        self.entThrusterSpeed4Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed4, background="pink",font=self.customFont)
        self.entThrusterSpeed5Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed5, background="pink",font=self.customFont)
        self.entThrusterSpeed6Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed6, background="pink",font=self.customFont)
        self.entThrusterSpeed7Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed7, background="pink",font=self.customFont)
        self.entThrusterSpeed8Data = Entry(groupThrusterSpeed, textvariable=self.vThrusterSpeed8, background="pink",font=self.customFont)
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



		#controller

        # frame container
        frameAtt1 = Frame(frameController, bg='white')
        frameAtt1.grid(row=0, column=0,sticky=N,padx=15,pady=15)
        # grouping
        groupAtt1 = LabelFrame(frameAtt1, text="Attitude Information", font=self.customFont)
        groupAtt1.pack()
        # widget definitions
        lblDepth = Label(groupAtt1, text="Depth:", font=self.customFont)
        lblHeading = Label(groupAtt1, text="Heading:", font=self.customFont)
        lblForward = Label(groupAtt1, text="Forward:", font=self.customFont)
        lblSideMove = Label(groupAtt1,text="Side move:",font=self.customFont)
        lblForwardVelocity=Label(groupAtt1,text="Forward Velocity:",font=self.customFont)
        lblSideVelocity=Label(groupAtt1,text="Side Velocity:",font=self.customFont)
        # initialize variables
        self.vDepth = StringVar()
        self.vDepth.set("Depth-data")
        self.vHeading = StringVar()
        self.vHeading.set("Heading-data")
        self.vForward = StringVar()
        self.vForward.set("Forward-data")
        self.vSideMove = StringVar()
        self.vSideMove.set("SideMove-data")
        self.vForwardVelocity=StringVar()
        self.vForwardVelocity.set("Forward velocity-data")
        self.vSideVelocity=StringVar()
        self.vSideVelocity.set("Side Velocity-data")

        # associate variables with labels displaying data
        self.lblDepthData = Entry(groupAtt1, textvariable=self.vDepth, background="pink", font=self.customFont)
        self.lblHeadingData = Entry(groupAtt1, textvariable=self.vHeading, background="pink", font=self.customFont)
        self.lblForwardData = Entry(groupAtt1, textvariable=self.vForward, background="pink", font=self.customFont)
        self.lblSideMoveData = Entry(groupAtt1,textvariable=self.vSideMove,background="pink",font=self.customFont)
        self.lblForwardVelocitydata=Entry(groupAtt1,textvariable=self.vForwardVelocity,background="pink",font=self.customFont)
        self.lblSideVelocity=Entry(groupAtt1,textvariable=self.vSideVelocity,background="pink",font=self.customFont)
        # layout widgets
        lblDepth.grid(row=0,sticky=W,padx=5,pady=5)
        lblHeading.grid(row=1,sticky=W,padx=5,pady=5)
        lblForward.grid(row=2,sticky=W,padx=5,pady=5)

        lblSideMove.grid(row=3,sticky=W,padx=5,pady=5)
        lblForwardVelocity.grid(row=4,sticky=W,padx=5,pady=5)
        lblSideVelocity.grid(row=5,sticky=W,padx=5,pady=5)
        self.lblDepthData.grid(row=0, column=1)
        self.lblHeadingData.grid(row=1, column=1)
        self.lblForwardData.grid(row=2, column=1)
        self.lblSideMoveData.grid(row=3,column=1)
        self.lblForwardVelocitydata.grid(row=4,column=1)
        self.lblSideVelocity.grid(row=5,column=1)

        #goal
        # grouping
        frameAtt2 = Frame(frameController, bg='white')
        frameAtt2.grid(row=0, column=1,sticky=N,padx=15,pady=15)
        groupAtt2 = LabelFrame(frameAtt2, text="Goal", font=self.customFont)
        bstartgoal= Button(groupAtt2,text= "Start Goal",background='pink' ,command=printgoal)
        bendgoal = Button(groupAtt2, text="End Goal",background='pink' , command=endgoal)

        bdisablepid = Button(groupAtt2, text="Disable Pid", background='pink' ,command=disablepid)
        bstartgoal.grid(row=1,sticky=W,padx=5,pady=5)
        bendgoal.grid(row=2,sticky=W,padx=5,pady=5)
        bdisablepid.grid(row=3,sticky=W,padx=5,pady=5)
        groupAtt2.pack()

        #action
        #grouping
        frameAtt3 =Frame(frameController,bg='white')
        frameAtt3.grid(row=0,column=2,sticky=N,padx=15,pady=15)
        groupAtt3 = LabelFrame(frameAtt3,text="action",font=self.customFont)
        bhover= Button(groupAtt3,text="Hover",background='pink',command=printhover)
        bsurface= Button(groupAtt3,text="Surface",background='pink',command=printsurface)
        bhomebase=Button(groupAtt3,text="Home base",background='pink',command=printhomebase)
        bhover.grid(row=1,sticky=W,padx=5,pady=5)
        bsurface.grid(row=2,sticky=W,padx=5,pady=5)
        bhomebase.grid(row=3,sticky=W,padx=5,pady=5)
        groupAtt3.pack()

        #navigation
        #grouping
        frameAtt4= Frame(frameController,bg='white')
        frameAtt4.grid(row=1,column=0,sticky=W,padx=15,pady=15)
        groupAtt4 = LabelFrame(frameAtt4,text="Navigation",font=self.customFont)
        lblxcoordinate = Label(groupAtt4,text="X-Coordinate:", font=self.customFont)
        lblycoordinate = Label(groupAtt4, text="Y-Coordinate:", font=self.customFont)
        xinput= Entry(groupAtt4)
        yinput= Entry(groupAtt4)
        go=Button(groupAtt4,text="Go",font=self.customFont,command=printgo)
        lblxcoordinate.grid(row=1)
        lblycoordinate.grid(row=2)
        go.grid(row=3)
        xinput.grid(row=1,column=2)
        yinput.grid(row=2,column=2)
        groupAtt4.pack()



	rospy.Subscriber('controllerdata', controller, self.controller_callback)
	rospy.Subscriber('depthdata', depth, self.depth_callback)
	rospy.Subscriber('velocitydata',velocity,self.velocity_callback)

        rospy.Subscriber('temperaturedata', temperature, self.temp_callback)
        rospy.Subscriber('batterydata', battery, self.battery_callback)
        rospy.Subscriber('compassdata', compass_data, self.compass_callback)
    	rospy.Subscriber('positiondata', position, self.position_callback)
    	rospy.Subscriber('depthdata', depth, self.depth_callback)
    	rospy.Subscriber('hullstatusdata', hullstatus, self.hullstatus_callback)
    	rospy.Subscriber('controllerdata', controller, self.controller_callback)
    	rospy.Subscriber('thrusterdata', thruster, self.thruster_callback)


    def controller_callback(self, controllerparam):
        self.vHeading.set(str(round(controllerparam.heading_setpoint,2)))
        self.vForward.set(str(round(controllerparam.forward_setpoint,2)))
        self.vSideMove.set(str(round(controllerparam.sidemove_setpoint,2)))

    def depth_callback(self, depth):
        self.vDepth.set(str(round(depth.depth,2)))

    def velocity_callback(self, velocity):
	self.vForwardVelocity.set(str(round(velocity.ForwardVelocity,2)))
	self.vSideVelocity.set(str(round(velocity.SideVelocity,2)))



    def controller_callback(self, controllerparam):
        self.vHeading.set(str(round(controllerparam.heading_setpoint,2)))
        self.vForward.set(str(round(controllerparam.forward_setpoint,2)))
        self.vSideMove.set(str(round(controllerparam.sidemove_setpoint,2)))

    def depth_callback(self, depth):
        self.vDepth.set(str(round(depth.depth,2)))

    def velocity_callback(self, velocity):
	self.vForwardVelocity.set(str(round(velocity.ForwardVelocity,2)))
	self.vSideVelocity.set(str(round(velocity.SideVelocity,2)))


    def temp_callback(self,temp):
    	self.vTemp.set(str(round(temp.temp,2)))
        self.vCPUTemp.set(str(round(temp.cputemp,2)))
        self.vHumidity.set(str(round(temp.humidity,2)))

    def battery_callback(self, batt):
        self.vVolt.set(str(round(batt.volt,2)))
        self.vCurrent.set(str(round(batt.current,2)))
        self.vPercentUsed.set(str(round(batt.percentused,2)))

    def compass_callback(self, orientation):
        self.vYaw.set(str(round(orientation.yaw,2)))
        self.vPitch.set(str(round(orientation.pitch,2)))
        self.vRoll.set(str(round(orientation.roll,2)))

    def position_callback(self,pos):
        self.vPosX.set(str(round(pos.x,2)))
        self.vPosY.set(str(round(pos.y,2)))
        self.vRelPosX.set(round(pos.relx,2))
        self.vRelPosY.set(round(pos.rely,2))
        self.vRelPosZ.set(round(pos.relz,2))
        self.vVelX.set(round(pos.velx,2))
        self.vVelY.set(round(pos.vely,2))
        self.vVelZ.set(round(pos.velz,2))

    def depth_callback(self, depth):
        self.vDepth.set(str(round(depth.depth,2)))
        self.vPressure.set(str(round(depth.pressure/1000,2)))
        self.vAltitude.set(str(round(depth.altitude,2)))

    def hullstatus_callback(self, hull_status):
        self.vLeak1.set(str(hull_status.leak1))
        self.vLeak2.set(str(hull_status.leak2))
        self.vLeak3.set(str(hull_status.leak3))

    def controller_callback(self, controllerparam):
        self.vHeading.set(str(round(controllerparam.heading_setpoint,2)))
        self.vForward.set(str(round(controllerparam.forward_setpoint,2)))
        self.vSideMove.set(str(round(controllerparam.sidemove_setpoint,2)))
        self.vGoalDepth.set(str(round(controllerparam.depth_setpoint,2)))
        self.vGoalID.set(str(controllerparam.goal_id))
        self.vHeadingErr.set(str(round(controllerparam.heading_error,2)))
        self.vForwardErr.set(str(round(controllerparam.forward_error,2)))
        self.vSideMoveErr.set(str(round(controllerparam.sidemove_error,2)))
        self.vGoalDepthErr.set(str(round(controllerparam.depth_error,2)))
        self.vGoalStatus.set(str(controllerparam.status))

    def thruster_callback(self,thrusters):
        self.vThrusterSpeed1.set(str(round(thrusters.speed1,2)))
        self.vThrusterSpeed2.set(str(round(thrusters.speed2,2)))
        self.vThrusterSpeed3.set(str(round(thrusters.speed3,2)))
        self.vThrusterSpeed4.set(str(round(thrusters.speed4,2)))
        self.vThrusterSpeed5.set(str(round(thrusters.speed5,2)))
        self.vThrusterSpeed6.set(str(round(thrusters.speed6,2)))
        self.vThrusterSpeed7.set(str(round(thrusters.speed7,2)))
        self.vThrusterSpeed8.set(str(round(thrusters.speed8,2)))



if __name__ == '__main__':
    rospy.init_node('gui', anonymous=True)
    root = Tk()
    myGui = ListenGui(root)
    root.mainloop()
