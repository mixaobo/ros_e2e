;; Auto-generated. Do not edit!


(when (boundp 'ros_basics_turorials::Localize)
  (if (not (find-package "ROS_BASICS_TURORIALS"))
    (make-package "ROS_BASICS_TURORIALS"))
  (shadow 'Localize (find-package "ROS_BASICS_TURORIALS")))
(unless (find-package "ROS_BASICS_TURORIALS::LOCALIZE")
  (make-package "ROS_BASICS_TURORIALS::LOCALIZE"))

(in-package "ROS")
;;//! \htmlinclude Localize.msg.html


(defclass ros_basics_turorials::Localize
  :super ros::object
  :slots (_Distance _AoA ))

(defmethod ros_basics_turorials::Localize
  (:init
   (&key
    ((:Distance __Distance) 0.0)
    ((:AoA __AoA) 0.0)
    )
   (send-super :init)
   (setq _Distance (float __Distance))
   (setq _AoA (float __AoA))
   self)
  (:Distance
   (&optional __Distance)
   (if __Distance (setq _Distance __Distance)) _Distance)
  (:AoA
   (&optional __AoA)
   (if __AoA (setq _AoA __AoA)) _AoA)
  (:serialization-length
   ()
   (+
    ;; float64 _Distance
    8
    ;; float64 _AoA
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _Distance
       (sys::poke _Distance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _AoA
       (sys::poke _AoA (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _Distance
     (setq _Distance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _AoA
     (setq _AoA (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get ros_basics_turorials::Localize :md5sum-) "fdd62682e37010cc81e982ba74365e59")
(setf (get ros_basics_turorials::Localize :datatype-) "ros_basics_turorials/Localize")
(setf (get ros_basics_turorials::Localize :definition-)
      "float64 Distance
float64 AoA


")



(provide :ros_basics_turorials/Localize "fdd62682e37010cc81e982ba74365e59")


