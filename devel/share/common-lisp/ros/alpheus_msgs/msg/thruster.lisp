; Auto-generated. Do not edit!


(cl:in-package alpheus_msgs-msg)


;//! \htmlinclude thruster.msg.html

(cl:defclass <thruster> (roslisp-msg-protocol:ros-message)
  ((speedfwd1
    :reader speedfwd1
    :initarg :speedfwd1
    :type cl:fixnum
    :initform 0)
   (speedfwd2
    :reader speedfwd2
    :initarg :speedfwd2
    :type cl:fixnum
    :initform 0)
   (speedup1
    :reader speedup1
    :initarg :speedup1
    :type cl:fixnum
    :initform 0)
   (speedup2
    :reader speedup2
    :initarg :speedup2
    :type cl:fixnum
    :initform 0)
   (speedup3
    :reader speedup3
    :initarg :speedup3
    :type cl:fixnum
    :initform 0)
   (speedup4
    :reader speedup4
    :initarg :speedup4
    :type cl:fixnum
    :initform 0)
   (speeddir1
    :reader speeddir1
    :initarg :speeddir1
    :type cl:fixnum
    :initform 0)
   (speeddir2
    :reader speeddir2
    :initarg :speeddir2
    :type cl:fixnum
    :initform 0))
)

(cl:defclass thruster (<thruster>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <thruster>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'thruster)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name alpheus_msgs-msg:<thruster> is deprecated: use alpheus_msgs-msg:thruster instead.")))

(cl:ensure-generic-function 'speedfwd1-val :lambda-list '(m))
(cl:defmethod speedfwd1-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedfwd1-val is deprecated.  Use alpheus_msgs-msg:speedfwd1 instead.")
  (speedfwd1 m))

(cl:ensure-generic-function 'speedfwd2-val :lambda-list '(m))
(cl:defmethod speedfwd2-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedfwd2-val is deprecated.  Use alpheus_msgs-msg:speedfwd2 instead.")
  (speedfwd2 m))

(cl:ensure-generic-function 'speedup1-val :lambda-list '(m))
(cl:defmethod speedup1-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedup1-val is deprecated.  Use alpheus_msgs-msg:speedup1 instead.")
  (speedup1 m))

(cl:ensure-generic-function 'speedup2-val :lambda-list '(m))
(cl:defmethod speedup2-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedup2-val is deprecated.  Use alpheus_msgs-msg:speedup2 instead.")
  (speedup2 m))

(cl:ensure-generic-function 'speedup3-val :lambda-list '(m))
(cl:defmethod speedup3-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedup3-val is deprecated.  Use alpheus_msgs-msg:speedup3 instead.")
  (speedup3 m))

(cl:ensure-generic-function 'speedup4-val :lambda-list '(m))
(cl:defmethod speedup4-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speedup4-val is deprecated.  Use alpheus_msgs-msg:speedup4 instead.")
  (speedup4 m))

(cl:ensure-generic-function 'speeddir1-val :lambda-list '(m))
(cl:defmethod speeddir1-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speeddir1-val is deprecated.  Use alpheus_msgs-msg:speeddir1 instead.")
  (speeddir1 m))

(cl:ensure-generic-function 'speeddir2-val :lambda-list '(m))
(cl:defmethod speeddir2-val ((m <thruster>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader alpheus_msgs-msg:speeddir2-val is deprecated.  Use alpheus_msgs-msg:speeddir2 instead.")
  (speeddir2 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <thruster>) ostream)
  "Serializes a message object of type '<thruster>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedfwd1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedfwd1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedfwd2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedfwd2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup3)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup4)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speeddir1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speeddir1)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speeddir2)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speeddir2)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <thruster>) istream)
  "Deserializes a message object of type '<thruster>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedfwd1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedfwd1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedfwd2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedfwd2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup3)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speedup4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speedup4)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speeddir1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speeddir1)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'speeddir2)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'speeddir2)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<thruster>)))
  "Returns string type for a message object of type '<thruster>"
  "alpheus_msgs/thruster")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'thruster)))
  "Returns string type for a message object of type 'thruster"
  "alpheus_msgs/thruster")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<thruster>)))
  "Returns md5sum for a message object of type '<thruster>"
  "016d61562410ee3b17201a66aa29be18")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'thruster)))
  "Returns md5sum for a message object of type 'thruster"
  "016d61562410ee3b17201a66aa29be18")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<thruster>)))
  "Returns full string definition for message of type '<thruster>"
  (cl:format cl:nil "uint16 speedfwd1~%uint16 speedfwd2~%uint16 speedup1~%uint16 speedup2~%uint16 speedup3~%uint16 speedup4~%uint16 speeddir1~%uint16 speeddir2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'thruster)))
  "Returns full string definition for message of type 'thruster"
  (cl:format cl:nil "uint16 speedfwd1~%uint16 speedfwd2~%uint16 speedup1~%uint16 speedup2~%uint16 speedup3~%uint16 speedup4~%uint16 speeddir1~%uint16 speeddir2~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <thruster>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <thruster>))
  "Converts a ROS message object to a list"
  (cl:list 'thruster
    (cl:cons ':speedfwd1 (speedfwd1 msg))
    (cl:cons ':speedfwd2 (speedfwd2 msg))
    (cl:cons ':speedup1 (speedup1 msg))
    (cl:cons ':speedup2 (speedup2 msg))
    (cl:cons ':speedup3 (speedup3 msg))
    (cl:cons ':speedup4 (speedup4 msg))
    (cl:cons ':speeddir1 (speeddir1 msg))
    (cl:cons ':speeddir2 (speeddir2 msg))
))
