; Auto-generated. Do not edit!


(cl:in-package alpheus_msgs-msg)


;//! \htmlinclude headingPID.msg.html

(cl:defclass <headingPID> (roslisp-msg-protocol:ros-message)
  ((hKp
    :reader hKp
    :initarg :hKp
    :type cl:float
    :initform 0.0)
   (hKi
    :reader hKi
    :initarg :hKi
    :type cl:float
    :initform 0.0)
   (hKd
    :reader hKd
    :initarg :hKd
    :type cl:float
    :initform 0.0))
)

(cl:defclass headingPID (<headingPID>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <headingPID>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'headingPID)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name alpheus_msgs-msg:<headingPID> is deprecated: use alpheus_msgs-msg:headingPID instead.")))

(cl:ensure-generic-function 'hKp-val :lambda-list '(m))
(cl:defmethod hKp-val ((m <headingPID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:hKp-val is deprecated.  Use alpheus_msgs-msg:hKp instead.")
  (hKp m))

(cl:ensure-generic-function 'hKi-val :lambda-list '(m))
(cl:defmethod hKi-val ((m <headingPID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:hKi-val is deprecated.  Use alpheus_msgs-msg:hKi instead.")
  (hKi m))

(cl:ensure-generic-function 'hKd-val :lambda-list '(m))
(cl:defmethod hKd-val ((m <headingPID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:hKd-val is deprecated.  Use alpheus_msgs-msg:hKd instead.")
  (hKd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <headingPID>) ostream)
  "Serializes a message object of type '<headingPID>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'hKp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'hKi))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'hKd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <headingPID>) istream)
  "Deserializes a message object of type '<headingPID>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'hKp) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'hKi) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'hKd) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<headingPID>)))
  "Returns string type for a message object of type '<headingPID>"
  "alpheus_msgs/headingPID")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'headingPID)))
  "Returns string type for a message object of type 'headingPID"
  "alpheus_msgs/headingPID")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<headingPID>)))
  "Returns md5sum for a message object of type '<headingPID>"
  "19a0fa31de3cf3c925595e656db1566d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'headingPID)))
  "Returns md5sum for a message object of type 'headingPID"
  "19a0fa31de3cf3c925595e656db1566d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<headingPID>)))
  "Returns full string definition for message of type '<headingPID>"
  (cl:format cl:nil "float32 hKp~%float32 hKi~%float32 hKd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'headingPID)))
  "Returns full string definition for message of type 'headingPID"
  (cl:format cl:nil "float32 hKp~%float32 hKi~%float32 hKd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <headingPID>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <headingPID>))
  "Converts a ROS message object to a list"
  (cl:list 'headingPID
    (cl:cons ':hKp (hKp msg))
    (cl:cons ':hKi (hKi msg))
    (cl:cons ':hKd (hKd msg))
))
