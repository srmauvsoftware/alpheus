;; Auto-generated. Do not edit!


(when (boundp 'alpheus_msgs::headingPID)
  (if (not (find-package "ALPHEUS_MSGS"))
    (make-package "ALPHEUS_MSGS"))
  (shadow 'headingPID (find-package "ALPHEUS_MSGS")))
(unless (find-package "ALPHEUS_MSGS::HEADINGPID")
  (make-package "ALPHEUS_MSGS::HEADINGPID"))

(in-package "ROS")
;;//! \htmlinclude headingPID.msg.html


(defclass alpheus_msgs::headingPID
  :super ros::object
  :slots (_hKp _hKi _hKd ))

(defmethod alpheus_msgs::headingPID
  (:init
   (&key
    ((:hKp __hKp) 0.0)
    ((:hKi __hKi) 0.0)
    ((:hKd __hKd) 0.0)
    )
   (send-super :init)
   (setq _hKp (float __hKp))
   (setq _hKi (float __hKi))
   (setq _hKd (float __hKd))
   self)
  (:hKp
   (&optional __hKp)
   (if __hKp (setq _hKp __hKp)) _hKp)
  (:hKi
   (&optional __hKi)
   (if __hKi (setq _hKi __hKi)) _hKi)
  (:hKd
   (&optional __hKd)
   (if __hKd (setq _hKd __hKd)) _hKd)
  (:serialization-length
   ()
   (+
    ;; float32 _hKp
    4
    ;; float32 _hKi
    4
    ;; float32 _hKd
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _hKp
       (sys::poke _hKp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _hKi
       (sys::poke _hKi (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _hKd
       (sys::poke _hKd (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _hKp
     (setq _hKp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _hKi
     (setq _hKi (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _hKd
     (setq _hKd (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get alpheus_msgs::headingPID :md5sum-) "19a0fa31de3cf3c925595e656db1566d")
(setf (get alpheus_msgs::headingPID :datatype-) "alpheus_msgs/headingPID")
(setf (get alpheus_msgs::headingPID :definition-)
      "float32 hKp
float32 hKi
float32 hKd

")



(provide :alpheus_msgs/headingPID "19a0fa31de3cf3c925595e656db1566d")


