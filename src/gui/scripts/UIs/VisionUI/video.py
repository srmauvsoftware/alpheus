#!/usr/bin/env python
try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

from sensor_msgs.msg import Image
from PIL import Image
from PIl import ImageTk
import threading
import datetime
import imutils
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class Video:
    def __init__(self, vs, frame, outputPath):
        self.vs = vs
        self.outputPath = outputPath
        self.thread = None
        self.stopEvent = None
        self.panel = frame

        self.stopEvent = threading.Event()
        self.thread = threading.Thread(target=self.videoLoop, args=())
        self.thread.start()

        self.root.wm_title("Alpheus Front Cam")
        self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)

        def videoLoop(self):
            try:
                while not self.stopEvent.is_set()
                self.frame = self.vs.read()
                self.frame = imutils.reseize(self.frame, width=300)
