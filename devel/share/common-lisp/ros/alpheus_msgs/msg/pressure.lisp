; Auto-generated. Do not edit!


(cl:in-package alpheus_msgs-msg)


;//! \htmlinclude pressure.msg.html

(cl:defclass <pressure> (roslisp-msg-protocol:ros-message)
  ((pressure
    :reader pressure
    :initarg :pressure
    :type cl:float
    :initform 0.0))
)

(cl:defclass pressure (<pressure>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pressure>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pressure)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name alpheus_msgs-msg:<pressure> is deprecated: use alpheus_msgs-msg:pressure instead.")))

(cl:ensure-generic-function 'pressure-val :lambda-list '(m))
(cl:defmethod pressure-val ((m <pressure>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:pressure-val is deprecated.  Use alpheus_msgs-msg:pressure instead.")
  (pressure m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pressure>) ostream)
  "Serializes a message object of type '<pressure>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'pressure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pressure>) istream)
  "Deserializes a message object of type '<pressure>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'pressure) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pressure>)))
  "Returns string type for a message object of type '<pressure>"
  "alpheus_msgs/pressure")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pressure)))
  "Returns string type for a message object of type 'pressure"
  "alpheus_msgs/pressure")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pressure>)))
  "Returns md5sum for a message object of type '<pressure>"
  "d08eeab8c09d2ba14f8144e3bbf40d21")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pressure)))
  "Returns md5sum for a message object of type 'pressure"
  "d08eeab8c09d2ba14f8144e3bbf40d21")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pressure>)))
  "Returns full string definition for message of type '<pressure>"
  (cl:format cl:nil "float32 pressure~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pressure)))
  "Returns full string definition for message of type 'pressure"
  (cl:format cl:nil "float32 pressure~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pressure>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pressure>))
  "Converts a ROS message object to a list"
  (cl:list 'pressure
    (cl:cons ':pressure (pressure msg))
))
