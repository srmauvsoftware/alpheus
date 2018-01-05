; Auto-generated. Do not edit!


(cl:in-package alpheus_msgs-msg)


;//! \htmlinclude offsetData.msg.html

(cl:defclass <offsetData> (roslisp-msg-protocol:ros-message)
  ((offsetX
    :reader offsetX
    :initarg :offsetX
    :type cl:float
    :initform 0.0)
   (offsetY
    :reader offsetY
    :initarg :offsetY
    :type cl:float
    :initform 0.0))
)

(cl:defclass offsetData (<offsetData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <offsetData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'offsetData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name alpheus_msgs-msg:<offsetData> is deprecated: use alpheus_msgs-msg:offsetData instead.")))

(cl:ensure-generic-function 'offsetX-val :lambda-list '(m))
(cl:defmethod offsetX-val ((m <offsetData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:offsetX-val is deprecated.  Use alpheus_msgs-msg:offsetX instead.")
  (offsetX m))

(cl:ensure-generic-function 'offsetY-val :lambda-list '(m))
(cl:defmethod offsetY-val ((m <offsetData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:offsetY-val is deprecated.  Use alpheus_msgs-msg:offsetY instead.")
  (offsetY m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <offsetData>) ostream)
  "Serializes a message object of type '<offsetData>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'offsetX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'offsetY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <offsetData>) istream)
  "Deserializes a message object of type '<offsetData>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'offsetX) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'offsetY) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<offsetData>)))
  "Returns string type for a message object of type '<offsetData>"
  "alpheus_msgs/offsetData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'offsetData)))
  "Returns string type for a message object of type 'offsetData"
  "alpheus_msgs/offsetData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<offsetData>)))
  "Returns md5sum for a message object of type '<offsetData>"
  "796ae190d97828899df8883bfe807076")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'offsetData)))
  "Returns md5sum for a message object of type 'offsetData"
  "796ae190d97828899df8883bfe807076")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<offsetData>)))
  "Returns full string definition for message of type '<offsetData>"
  (cl:format cl:nil "float32 offsetX~%float32 offsetY~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'offsetData)))
  "Returns full string definition for message of type 'offsetData"
  (cl:format cl:nil "float32 offsetX~%float32 offsetY~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <offsetData>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <offsetData>))
  "Converts a ROS message object to a list"
  (cl:list 'offsetData
    (cl:cons ':offsetX (offsetX msg))
    (cl:cons ':offsetY (offsetY msg))
))
