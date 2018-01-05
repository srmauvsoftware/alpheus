;; Auto-generated. Do not edit!


(when (boundp 'alpheus_msgs::pressure)
  (if (not (find-package "ALPHEUS_MSGS"))
    (make-package "ALPHEUS_MSGS"))
  (shadow 'pressure (find-package "ALPHEUS_MSGS")))
(unless (find-package "ALPHEUS_MSGS::PRESSURE")
  (make-package "ALPHEUS_MSGS::PRESSURE"))

(in-package "ROS")
;;//! \htmlinclude pressure.msg.html


(defclass alpheus_msgs::pressure
  :super ros::object
  :slots (_pressure ))

(defmethod alpheus_msgs::pressure
  (:init
   (&key
    ((:pressure __pressure) 0.0)
    )
   (send-super :init)
   (setq _pressure (float __pressure))
   self)
  (:pressure
   (&optional __pressure)
   (if __pressure (setq _pressure __pressure)) _pressure)
  (:serialization-length
   ()
   (+
    ;; float32 _pressure
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _pressure
       (sys::poke _pressure (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _pressure
     (setq _pressure (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get alpheus_msgs::pressure :md5sum-) "d08eeab8c09d2ba14f8144e3bbf40d21")
(setf (get alpheus_msgs::pressure :datatype-) "alpheus_msgs/pressure")
(setf (get alpheus_msgs::pressure :definition-)
      "float32 pressure

")



(provide :alpheus_msgs/pressure "d08eeab8c09d2ba14f8144e3bbf40d21")


