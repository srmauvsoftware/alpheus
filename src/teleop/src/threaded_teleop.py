#!/usr/bin/env python
# import roslib; roslib.load_manifest('teleop')
import roslib
import rospy

from alpheus_msgs.msg import depthThruster
from alpheus_msgs.msg import vectorThruster

import sys, select, termios, tty, threading

msg = """
Alpheus Testing Mode - Reading From Keyboard
--------------------
Arrow Key Up - Forward
Arrow Key Down - Backward
Arrow Key Right - Right
Arrow Key Left - Left
Key W - Depth UP
Key S - Depth Down
--------------------
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def depthMovement():
    while(1):
        key = getKey()
        dt = depthThruster()
        if key == 'W':
            dt.td1 = 1100
            dt.td2 = 1100
            dt.td3 = 1100
            dt.td4 = 1100
            print("Moving Up")
        elif key == 'S':
            dt.td1 = 1900
            dt.td2 = 1900
            dt.td3 = 1900
            dt.td4 = 1900
            print("Moving Down")

        elif key == 'Q':
            print("Quitting")
            break

        depthPub.publish(dt)

def vectorMovement():
    while(1):
        key = getKey()
        vt = vectorThruster()
        if key == 'A':
            vt.tfl = 1900
            vt.trl = 1900
            vt.tfr = 1900
            vt.trr = 1900
            print("Moving forward")

        elif key == 'B':
            vt.tfl = 1100
            vt.tfr = 1100
            vt.trl = 1100
            vt.trr = 1100
            print("Moving backward")

        elif key == 'D':
            vt.tfl = 1100
            vt.tfr = 1900
            vt.trl = 1900
            vt.trr = 1100
            print("Moving left")

        elif key == 'C':
            vt.tfl = 1900
            vt.tfr = 1100
            vt.trl = 1100
            vt.trr = 1900
            print("Moving right")

        vectorPub.publish(vt)

if __name__=="__main__":
    print(msg)
    settings = termios.tcgetattr(sys.stdin)
    
    depthPub = rospy.Publisher('/thruster/depth', depthThruster, queue_size=1)
    vectorPub = rospy.Publisher('/thruster/vector', vectorThruster, queue_size=1)
    
    try:
        depthThread = threading.Thread(target=depthMovement)
        vectorThread = threading.Thread(target=vectorMovement)
        rospy.init_node('teleop')
	depthThread.start()
	vectorThread.start()
        
    except rospy.ROSInterruptException:
        pass
    
    finally:
        dt = depthThruster()
        vt = vectorThruster()
        dt.td1 = 1500
        dt.td2 = 1500
        dt.td3 = 1500
        dt.td4 = 1500
        vt.tfl = 1500
        vt.tfr = 1500
        vt.trl = 1500
        vt.trr = 1500
        vt.tfl = 1500
        depthPub.publish(dt)
        vectorPub.publish(vt)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
