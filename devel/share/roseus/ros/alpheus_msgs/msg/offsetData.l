;; Auto-generated. Do not edit!


(when (boundp 'alpheus_msgs::offsetData)
  (if (not (find-package "ALPHEUS_MSGS"))
    (make-package "ALPHEUS_MSGS"))
  (shadow 'offsetData (find-package "ALPHEUS_MSGS")))
(unless (find-package "ALPHEUS_MSGS::OFFSETDATA")
  (make-package "ALPHEUS_MSGS::OFFSETDATA"))

(in-package "ROS")
;;//! \htmlinclude offsetData.msg.html


(defclass alpheus_msgs::offsetData
  :super ros::object
  :slots (_offsetX _offsetY ))

(defmethod alpheus_msgs::offsetData
  (:init
   (&key
    ((:offsetX __offsetX) 0.0)
    ((:offsetY __offsetY) 0.0)
    )
   (send-super :init)
   (setq _offsetX (float __offsetX))
   (setq _offsetY (float __offsetY))
   self)
  (:offsetX
   (&optional __offsetX)
   (if __offsetX (setq _offsetX __offsetX)) _offsetX)
  (:offsetY
   (&optional __offsetY)
   (if __offsetY (setq _offsetY __offsetY)) _offsetY)
  (:serialization-length
   ()
   (+
    ;; float32 _offsetX
    4
    ;; float32 _offsetY
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _offsetX
       (sys::poke _offsetX (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _offsetY
       (sys::poke _offsetY (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _offsetX
     (setq _offsetX (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _offsetY
     (setq _offsetY (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get alpheus_msgs::offsetData :md5sum-) "796ae190d97828899df8883bfe807076")
(setf (get alpheus_msgs::offsetData :datatype-) "alpheus_msgs/offsetData")
(setf (get alpheus_msgs::offsetData :definition-)
      "float32 offsetX
float32 offsetY

")



(provide :alpheus_msgs/offsetData "796ae190d97828899df8883bfe807076")


