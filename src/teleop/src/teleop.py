#!/usr/bin/env python
import roslib; roslib.load_manifest('teleop')
import rospy

from alpheus_msgs.msg import thruster

import sys, select, termios, tty

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

if __name__=="__main__":
    print(msg)
    settings = termios.tcgetattr(sys.stdin)

    pub = rospy.Publisher('/thruster', thruster, queue_size=1)
    rospy.init_node('teleop')

    try:
        while(1):
            key = getKey()
            t = thruster()
            if key == 'A':
                t.speedfwd1 = 1900
                t.speedfwd2 = 1900
                print("Moving Forward")
            elif key == 'B':
                t.speedfwd1 = 1100
                t.speedfwd2 = 1100
                print("Moving Backward")
            elif key == 'C':
                t.speeddir1 = 1900
                t.speeddir2 = 1100
                print("Moving Right")
            elif key == 'D':
                t.speeddir1 = 1100
                t.speeddir2 = 1900
                print("Moving Left")
            elif key == 'w':
                t.speedup1 = 1100
                t.speedup2 = 1100
                t.speedup3 = 1100
                t.speedup4 = 1100
                print("Moving Up")
            elif key == 's':
                t.speedup1 = 1900
                t.speedup2 = 1900
                t.speedup3 = 1900
                t.speedup4 = 1900
                print("Moving Down")

            elif key == 'q':
                print("Quitting")
                break

            else:
                t.speedup1 = 1500
                t.speedup2 = 1500
                t.speedup3 = 1500
                t.speedup4 = 1500
                t.speedfwd1 = 1500
                t.speedfwd2 = 1500
                t.speeddir1 = 1500
                t.speeddir2 = 1500

            pub.publish(t)

    except Exception, e:
        print e

    finally:
        t = thruster()
        t.speedup1 = 1500
        t.speedup2 = 1500
        t.speedup3 = 1500
        t.speedup4 = 1500
        t.speedfwd1 = 1500
        t.speedfwd2 = 1500
        pub.publish(t)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
'''
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import tty, termios
import sys
if sys.version_info.major < 3:
    import thread as _thread
else:
    import _thread
import time


try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def keypress():
    global char
    char = getch()

def main():
    global char
    char = None
    _thread.start_new_thread(keypress, ())

    while True:
        if char is not None:
            try:
                print("Key pressed is " + char.decode('utf-8'))
            except UnicodeDecodeError:
                print("character can not be decoded, sorry!")
                char = None
            _thread.start_new_thread(keypress, ())
            if char == 'q' or char == '\x1b':  # x1b is ESC
                exit()
            char = None
        print("Program is running")
        time.sleep(1)

if __name__ == "__main__":
    main()
'''
