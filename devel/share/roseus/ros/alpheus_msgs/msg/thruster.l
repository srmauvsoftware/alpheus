;; Auto-generated. Do not edit!


(when (boundp 'alpheus_msgs::thruster)
  (if (not (find-package "ALPHEUS_MSGS"))
    (make-package "ALPHEUS_MSGS"))
  (shadow 'thruster (find-package "ALPHEUS_MSGS")))
(unless (find-package "ALPHEUS_MSGS::THRUSTER")
  (make-package "ALPHEUS_MSGS::THRUSTER"))

(in-package "ROS")
;;//! \htmlinclude thruster.msg.html


(defclass alpheus_msgs::thruster
  :super ros::object
  :slots (_speedfwd1 _speedfwd2 _speedup1 _speedup2 _speedup3 _speedup4 _speeddir1 _speeddir2 ))

(defmethod alpheus_msgs::thruster
  (:init
   (&key
    ((:speedfwd1 __speedfwd1) 0)
    ((:speedfwd2 __speedfwd2) 0)
    ((:speedup1 __speedup1) 0)
    ((:speedup2 __speedup2) 0)
    ((:speedup3 __speedup3) 0)
    ((:speedup4 __speedup4) 0)
    ((:speeddir1 __speeddir1) 0)
    ((:speeddir2 __speeddir2) 0)
    )
   (send-super :init)
   (setq _speedfwd1 (round __speedfwd1))
   (setq _speedfwd2 (round __speedfwd2))
   (setq _speedup1 (round __speedup1))
   (setq _speedup2 (round __speedup2))
   (setq _speedup3 (round __speedup3))
   (setq _speedup4 (round __speedup4))
   (setq _speeddir1 (round __speeddir1))
   (setq _speeddir2 (round __speeddir2))
   self)
  (:speedfwd1
   (&optional __speedfwd1)
   (if __speedfwd1 (setq _speedfwd1 __speedfwd1)) _speedfwd1)
  (:speedfwd2
   (&optional __speedfwd2)
   (if __speedfwd2 (setq _speedfwd2 __speedfwd2)) _speedfwd2)
  (:speedup1
   (&optional __speedup1)
   (if __speedup1 (setq _speedup1 __speedup1)) _speedup1)
  (:speedup2
   (&optional __speedup2)
   (if __speedup2 (setq _speedup2 __speedup2)) _speedup2)
  (:speedup3
   (&optional __speedup3)
   (if __speedup3 (setq _speedup3 __speedup3)) _speedup3)
  (:speedup4
   (&optional __speedup4)
   (if __speedup4 (setq _speedup4 __speedup4)) _speedup4)
  (:speeddir1
   (&optional __speeddir1)
   (if __speeddir1 (setq _speeddir1 __speeddir1)) _speeddir1)
  (:speeddir2
   (&optional __speeddir2)
   (if __speeddir2 (setq _speeddir2 __speeddir2)) _speeddir2)
  (:serialization-length
   ()
   (+
    ;; uint16 _speedfwd1
    2
    ;; uint16 _speedfwd2
    2
    ;; uint16 _speedup1
    2
    ;; uint16 _speedup2
    2
    ;; uint16 _speedup3
    2
    ;; uint16 _speedup4
    2
    ;; uint16 _speeddir1
    2
    ;; uint16 _speeddir2
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _speedfwd1
       (write-word _speedfwd1 s)
     ;; uint16 _speedfwd2
       (write-word _speedfwd2 s)
     ;; uint16 _speedup1
       (write-word _speedup1 s)
     ;; uint16 _speedup2
       (write-word _speedup2 s)
     ;; uint16 _speedup3
       (write-word _speedup3 s)
     ;; uint16 _speedup4
       (write-word _speedup4 s)
     ;; uint16 _speeddir1
       (write-word _speeddir1 s)
     ;; uint16 _speeddir2
       (write-word _speeddir2 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _speedfwd1
     (setq _speedfwd1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speedfwd2
     (setq _speedfwd2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speedup1
     (setq _speedup1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speedup2
     (setq _speedup2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speedup3
     (setq _speedup3 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speedup4
     (setq _speedup4 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speeddir1
     (setq _speeddir1 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _speeddir2
     (setq _speeddir2 (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get alpheus_msgs::thruster :md5sum-) "016d61562410ee3b17201a66aa29be18")
(setf (get alpheus_msgs::thruster :datatype-) "alpheus_msgs/thruster")
(setf (get alpheus_msgs::thruster :definition-)
      "uint16 speedfwd1
uint16 speedfwd2
uint16 speedup1
uint16 speedup2
uint16 speedup3
uint16 speedup4
uint16 speeddir1
uint16 speeddir2

")



(provide :alpheus_msgs/thruster "016d61562410ee3b17201a66aa29be18")


