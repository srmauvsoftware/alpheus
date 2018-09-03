class Gate:
    def __init__(self):
        self.img_type = rostopic.get_topic_type('/image/compressed')
        if self.img_type[0] == 'sensor_msgs/CompressedImage':
            self.imageSub = rospy.Subscriber("/image/compressed", CompressedImage, self.img_cb)

        elif self.img_type[0] == 'sensor_msgs/Image':
            self.imageSub = rospy.Subscriber("/alpheus_cam/front/image_raw", Image, self.img_cb)

        self.hsvSub = rospy.Subscriber("/hsv",hsv,self.hsvCallback)

        self.bridge = CvBridge()
        self.offsetData = offsetData()
        self.imagePub = rospy.Publisher("/front/gate", CompressedImage , queue_size=2)
        self.offsetPub = rospy.Publisher("/offsetData", offsetData, queue_size=2)
        self.erosion = None
        self.dilation = None
        self.cameraX = 640 / 2
        self.cameraY = 320 / 2
        self.r_hmin = 0
        self.r_smin = 0
        self.r_vmin = 0
        self.r_hmax = 0
        self.r_smax = 0
        self.r_vmax = 0
        self.g_hmin = 0
        self.g_smin = 0
        self.g_vmin = 0
        self.g_hmax = 0
        self.g_smax = 0
        self.g_vmax = 0

    def hsvCallback(self,data):

        rospy.loginfo("HSV data being subscribed: Hmin: " + str(data.hmin))

        if(data.color == 1):
            self.r_hmin = data.hmin
            self.r_smin = data.smin
            self.r_vmin = data.vmin
            self.r_hmax = data.hmax
            self.r_smax = data.smax
            self.r_vmax = data.vmax

        if(data.color == 2):
            self.g_hmin = data.hmin
            self.g_smin = data.smin
            self.g_vmin = data.vmin
            self.g_hmax = data.hmax
            self.g_smax = data.smax
            self.g_vmax = data.vmax

    def filter_image(self, cv_image):
        channels = cv2.split(cv_image)
        channels[0] = cv2.equalizeHist(channels[0])
        channels[1] = cv2.equalizeHist(channels[1])
        return cv2.merge(channels, cv_image)

    def largestContour(self, contours):
        areaArray = []
        for i, c in enumerate(contours):
            area = cv2.contourArea(c)
            areaArray.append(area)
        sorteddata = sorted(zip(areaArray, contours), key = lambda x: x[0], reverse=True)
        print(sorteddata[0][1])
        return sorteddata[0][1]

    def findOffsets(self, x, y):
        if( x < self.cameraX and y < self.cameraY ):
            offsetX = self.cameraX - x
            offsetY = self.cameraY - y
        elif( x > self.cameraX and y < self.cameraY ):
            offsetX = x - self.cameraX
            offsetY = self.cameraY - y
        elif( x < self.cameraX and y > self.cameraY):
            offsetX = self.cameraX - x
            offsetY = y - self.cameraY
        elif( x > self.cameraY and y > self.cameraY):
            offsetX = x - self.cameraX
            offsetY = y - self.cameraY
        return offsetX, offsetY

    def img_cb(self, data):
        if self.img_type[0] == 'sensor_msgs/CompressedImage':
            try:
                np_arr = np.fromstring(data.data, np.uint8)
                cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
            except CvBridgeError as e:
                print(e)

        elif self.img_type[0] == 'sensor_msgs/Image':
            try:
                cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            except CvBridgeError as e:
                print(e)

        print(self.rgb)
        print(self.r_hmin, self.r_smin, self.r_vmin)
        print(self.r_hmax, self.r_smax, self.r_vmax)
        print(self.g_hmin, self.g_smin, self.g_vmin)
        print(self.g_hmax, self.g_smax, self.g_vmax)
        lowerRed = np.array([ self.r_hmin, self.r_smin , self.r_vmin ], dtype=np.uint8)
        upperRed = np.array([ self.r_hmax, self.r_smax, self.r_vmax ], dtype=np.uint8)
        lowerGreen = np.array([ self.g_hmin, self.g_smin, self.g_vmin ], dtype=np.uint8)
        upperGreen = np.array([ self.g_hmax, self.g_smax, self.g_vmax ], dtype=np.uint8)

        #hsvRed = cv2.cvtColor(self.filter_image(cv_image), cv2.COLOR_BGR2HSV)
        #hsvGreen = cv2.cvtColor(self.filter_image(cv_image), cv2.COLOR_BGR2HSV)
        hsvRed = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        hsvGreen = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        maskRed = cv2.inRange(hsvRed, lowerRed, upperRed)
        maskGreen = cv2.inRange(hsvGreen, lowerGreen, upperGreen)

        if(self.erosion and self.dilation):
            erodeKernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(self.erosion, self.erosion))
            dilateKernel = cv2.getStructuringElement(cv2.MORPH_RECT,ksize=(self.dilation,self.dilation))
            cv2.erode(maskRed, erodeKernel, maskRed)
            cv2.erode(maskGreen, erodeKernel, maskGreen)
            cv2.dilate(maskRed, dilateKernel, maskRed)
            cv2.dilate(maskGreen, dilateKernel, maskGreen)

        contoursRed = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        contoursGreen = cv2.findContours(maskGreen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
        itr = -1
        a = 0
        self.offsetData.offsetX = 0
        self.offsetData.offsetY = 0
        if not contoursRed or contoursGreen:
            print("No Contours Found")
        else:
            cv2.circle(cv_image, (self.cameraX, self.cameraY), 3, (255, 255, 255), -1)
            if(self.rgb == 1):
                pipeRed = self.largestContour(contoursRed)
                Rx, Ry, Rh, Rw = cv2.boundingRect(pipeRed)
                redCenter = ( Rx + (Rw / 2) , Ry + (Rh / 2) )
                cv2.circle(cv_image, redCenter, 3, (255,0,0), -1)
                cv2.rectangle(cv_image, (Rx, Ry), (Rx + Rw, Ry + Rh), (255, 0, 0), 2)
                cv2.line(cv_image, (Rx+(Rw/2), Ry+(Rh/2)),(self.cameraX, self.cameraY),(255, 0, 0),3)

            if(self.rgb == 2):
                pipeGreen = self.largestContour(contoursGreen)
                Gx, Gy, Gh, Gw = cv2.boundingRect(pipeGreen)
                greenCenter = ( Gx + (Gw / 2) , Gy + (Gh / 2) )
                cv2.circle(cv_image, greenCenter, 3, (0,255,0), -1)
                cv2.rectangle(cv_image, (Gx, Gy), (Gx + Gw, Gy + Gh), (0, 255, 0), 2)
                cv2.line(cv_image, (Gx+(Gw/2), Gy+(Gh/2)),(self.cameraX, self.cameraY),(0, 255, 0),3)

            #if(redCenter and greenCenter):
            #    gateCenter = ( (redCenter[0] + greenCenter[0]) / 2 , (redCenter[1] + redCenter[1]) / 2 )
        #        gateCenter = findOffsets(gateCenter)
            #    self.offsetData.offsetX = gateCenter[0]
        #        self.offsetData.offsetY = gateCenter[1]

            #self.imagePub.publish(self.bridge.cv2_to_imgmsg(cv_image), "bgr8")
        msg = CompressedImage()
        msg.header.stamp = rospy.Time.now()
        msg.format = "jpeg"
        msg.data = np.array(cv2.imencode('.jpg', cv_image)[1]).tostring()
        self.imagePub.publish(msg)
        self.offsetPub.publish(self.offsetData)
