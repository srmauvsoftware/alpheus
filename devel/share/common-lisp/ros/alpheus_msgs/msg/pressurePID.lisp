; Auto-generated. Do not edit!


(cl:in-package alpheus_msgs-msg)


;//! \htmlinclude pressurePID.msg.html

(cl:defclass <pressurePID> (roslisp-msg-protocol:ros-message)
  ((pKp
    :reader pKp
    :initarg :pKp
    :type cl:float
    :initform 0.0)
   (pKi
    :reader pKi
    :initarg :pKi
    :type cl:float
    :initform 0.0)
   (pKd
    :reader pKd
    :initarg :pKd
    :type cl:float
    :initform 0.0))
)

(cl:defclass pressurePID (<pressurePID>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pressurePID>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pressurePID)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name alpheus_msgs-msg:<pressurePID> is deprecated: use alpheus_msgs-msg:pressurePID instead.")))

(cl:ensure-generic-function 'pKp-val :lambda-list '(m))
(cl:defmethod pKp-val ((m <pressurePID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:pKp-val is deprecated.  Use alpheus_msgs-msg:pKp instead.")
  (pKp m))

(cl:ensure-generic-function 'pKi-val :lambda-list '(m))
(cl:defmethod pKi-val ((m <pressurePID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:pKi-val is deprecated.  Use alpheus_msgs-msg:pKi instead.")
  (pKi m))

(cl:ensure-generic-function 'pKd-val :lambda-list '(m))
(cl:defmethod pKd-val ((m <pressurePID>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:pKd-val is deprecated.  Use alpheus_msgs-msg:pKd instead.")
  (pKd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pressurePID>) ostream)
  "Serializes a message object of type '<pressurePID>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pKp))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pKi))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pKd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pressurePID>) istream)
  "Deserializes a message object of type '<pressurePID>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pKp) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pKi) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pKd) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pressurePID>)))
  "Returns string type for a message object of type '<pressurePID>"
  "alpheus_msgs/pressurePID")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pressurePID)))
  "Returns string type for a message object of type 'pressurePID"
  "alpheus_msgs/pressurePID")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pressurePID>)))
  "Returns md5sum for a message object of type '<pressurePID>"
  "b607b6b53844bf703ffc3df5d628e627")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pressurePID)))
  "Returns md5sum for a message object of type 'pressurePID"
  "b607b6b53844bf703ffc3df5d628e627")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pressurePID>)))
  "Returns full string definition for message of type '<pressurePID>"
  (cl:format cl:nil "float32 pKp~%float32 pKi~%float32 pKd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pressurePID)))
  "Returns full string definition for message of type 'pressurePID"
  (cl:format cl:nil "float32 pKp~%float32 pKi~%float32 pKd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pressurePID>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pressurePID>))
  "Converts a ROS message object to a list"
  (cl:list 'pressurePID
    (cl:cons ':pKp (pKp msg))
    (cl:cons ':pKi (pKi msg))
    (cl:cons ':pKd (pKd msg))
))
