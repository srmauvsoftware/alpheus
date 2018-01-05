;; Auto-generated. Do not edit!


(when (boundp 'alpheus_msgs::pressurePID)
  (if (not (find-package "ALPHEUS_MSGS"))
    (make-package "ALPHEUS_MSGS"))
  (shadow 'pressurePID (find-package "ALPHEUS_MSGS")))
(unless (find-package "ALPHEUS_MSGS::PRESSUREPID")
  (make-package "ALPHEUS_MSGS::PRESSUREPID"))

(in-package "ROS")
;;//! \htmlinclude pressurePID.msg.html


(defclass alpheus_msgs::pressurePID
  :super ros::object
  :slots (_pKp _pKi _pKd ))

(defmethod alpheus_msgs::pressurePID
  (:init
   (&key
    ((:pKp __pKp) 0.0)
    ((:pKi __pKi) 0.0)
    ((:pKd __pKd) 0.0)
    )
   (send-super :init)
   (setq _pKp (float __pKp))
   (setq _pKi (float __pKi))
   (setq _pKd (float __pKd))
   self)
  (:pKp
   (&optional __pKp)
   (if __pKp (setq _pKp __pKp)) _pKp)
  (:pKi
   (&optional __pKi)
   (if __pKi (setq _pKi __pKi)) _pKi)
  (:pKd
   (&optional __pKd)
   (if __pKd (setq _pKd __pKd)) _pKd)
  (:serialization-length
   ()
   (+
    ;; float32 _pKp
    4
    ;; float32 _pKi
    4
    ;; float32 _pKd
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _pKp
       (sys::poke _pKp (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pKi
       (sys::poke _pKi (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _pKd
       (sys::poke _pKd (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _pKp
     (setq _pKp (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pKi
     (setq _pKi (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _pKd
     (setq _pKd (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get alpheus_msgs::pressurePID :md5sum-) "b607b6b53844bf703ffc3df5d628e627")
(setf (get alpheus_msgs::pressurePID :datatype-) "alpheus_msgs/pressurePID")
(setf (get alpheus_msgs::pressurePID :definition-)
      "float32 pKp
float32 pKi
float32 pKd

")



(provide :alpheus_msgs/pressurePID "b607b6b53844bf703ffc3df5d628e627")


