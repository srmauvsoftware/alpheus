#!/usr/bin/env python

from video import video

class bottomCamUI:
    def __init__(self, frameVideo):
        video(frameVideo, '/alpheus_cam/bottom/image_raw', 1, 1, 'Raw Image')
        video(frameVideo, '/alpheus_cam/bottom/image_processed', 1, 2, 'Processed Image')

    
