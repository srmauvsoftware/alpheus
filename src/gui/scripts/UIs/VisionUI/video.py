try:
    from Tkinter import *
    import ttk
    import tkFont
except ImportError:
    from tkinter import *
    import ttk
    import tkinter.font as tkFont

import PIL.Image
import PIL.ImageTk
import datetime
import imutils
import cv2
import rospy
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import numpy as np

'''
To Do -
* Implement Threading
* Path For Saving
'''

class video:
    def __init__(self, frameVideo, topic, row, column, name):
        self.row = row
        self.column = column
        rospy.Subscriber(topic, CompressedImage, self.image_cb)
        self.bridge = CvBridge()
        frame = Frame(frameVideo, bg='white')
        frame.grid(row=self.row, column=self.column, sticky=W, padx=15, pady=15)
        self.labelFrame = LabelFrame(frame, text=name, font="Helvetica 15 bold")
        self.panel = None
        snapButton = Button(self.labelFrame, text="Snapshot!",font="Helvetica",command = self.takeSnapshot).grid(column=column+1)
        self.labelFrame.pack()

    def image_cb(self, data):
        try:
            np_arr = np.fromstring(data.data, np.uint8)
            self.image_cv = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            '''
            image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image_cv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            '''
            image = imutils.resize(self.image_cv, width=300)
            image = PIL.Image.fromarray(image)
            image = PIL.ImageTk.PhotoImage(image)
            if self.panel is None:
                self.panel = Label(self.labelFrame, image=image)
                self.panel.image = image
                self.panel.grid(row=self.row, column=self.column+1, sticky=W, padx=15, pady=15)
            else:
                self.panel.configure(image=image)
                self.panel.image = image

        except CvBridgeError as e:
            print(e)

    def takeSnapshot(self):
        ts = datetime.datetime.now()
        filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
        cv2.imwrite(filename, self.image_cv)
        print("Image Saved")
