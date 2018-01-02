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
from video import video
from hsvDynClient import hsvDynClient

class frontCamUI:
    def __init__(self, frameVideo):
        video(frameVideo, '/alpheus_cam/front/image_raw', 1, 1, 'Raw Image')
        #video(frameVideo, '/alpheus_cam/front/image_processed', 1, 2, 'Processed Image')
        video(frameVideo, '/alpheus_cam/front/image_raw', 1, 2, 'Processed Image')
        hsvDynClient(frameVideo, 1, 3, 'HSV Range')
