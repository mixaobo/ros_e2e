;; Auto-generated. Do not edit!


(when (boundp 'ros_basics_turorials::CustomMsg)
  (if (not (find-package "ROS_BASICS_TURORIALS"))
    (make-package "ROS_BASICS_TURORIALS"))
  (shadow 'CustomMsg (find-package "ROS_BASICS_TURORIALS")))
(unless (find-package "ROS_BASICS_TURORIALS::CUSTOMMSG")
  (make-package "ROS_BASICS_TURORIALS::CUSTOMMSG"))

(in-package "ROS")
;;//! \htmlinclude CustomMsg.msg.html


(defclass ros_basics_turorials::CustomMsg
  :super ros::object
  :slots (_id _name ))

(defmethod ros_basics_turorials::CustomMsg
  (:init
   (&key
    ((:id __id) 0)
    ((:name __name) "")
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _name (string __name))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:serialization-length
   ()
   (+
    ;; int32 _id
    4
    ;; string _name
    4 (length _name)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _id
       (write-long _id s)
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get ros_basics_turorials::CustomMsg :md5sum-) "8fe5a440459dcada9c353c016dfb49d2")
(setf (get ros_basics_turorials::CustomMsg :datatype-) "ros_basics_turorials/CustomMsg")
(setf (get ros_basics_turorials::CustomMsg :definition-)
      "int32 id
string name
")



(provide :ros_basics_turorials/CustomMsg "8fe5a440459dcada9c353c016dfb49d2")


