;; Auto-generated. Do not edit!


(when (boundp 'ros_basics_turorials::AddTwoInts)
  (if (not (find-package "ROS_BASICS_TURORIALS"))
    (make-package "ROS_BASICS_TURORIALS"))
  (shadow 'AddTwoInts (find-package "ROS_BASICS_TURORIALS")))
(unless (find-package "ROS_BASICS_TURORIALS::ADDTWOINTS")
  (make-package "ROS_BASICS_TURORIALS::ADDTWOINTS"))
(unless (find-package "ROS_BASICS_TURORIALS::ADDTWOINTSREQUEST")
  (make-package "ROS_BASICS_TURORIALS::ADDTWOINTSREQUEST"))
(unless (find-package "ROS_BASICS_TURORIALS::ADDTWOINTSRESPONSE")
  (make-package "ROS_BASICS_TURORIALS::ADDTWOINTSRESPONSE"))

(in-package "ROS")





(defclass ros_basics_turorials::AddTwoIntsRequest
  :super ros::object
  :slots (_a _b ))

(defmethod ros_basics_turorials::AddTwoIntsRequest
  (:init
   (&key
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; int64 _a
    8
    ;; int64 _b
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _a
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _a (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _a) (= (length (_a . bv)) 2)) ;; bignum
              (write-long (ash (elt (_a . bv) 0) 0) s)
              (write-long (ash (elt (_a . bv) 1) -1) s))
             ((and (class _a) (= (length (_a . bv)) 1)) ;; big1
              (write-long (elt (_a . bv) 0) s)
              (write-long (if (>= _a 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _a s)(write-long (if (>= _a 0) 0 #xffffffff) s)))
     ;; int64 _b
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _b (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _b) (= (length (_b . bv)) 2)) ;; bignum
              (write-long (ash (elt (_b . bv) 0) 0) s)
              (write-long (ash (elt (_b . bv) 1) -1) s))
             ((and (class _b) (= (length (_b . bv)) 1)) ;; big1
              (write-long (elt (_b . bv) 0) s)
              (write-long (if (>= _b 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _b s)(write-long (if (>= _b 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _a
#+(or :alpha :irix6 :x86_64)
      (setf _a (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _a (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _b
#+(or :alpha :irix6 :x86_64)
      (setf _b (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _b (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass ros_basics_turorials::AddTwoIntsResponse
  :super ros::object
  :slots (_sum _testvalue ))

(defmethod ros_basics_turorials::AddTwoIntsResponse
  (:init
   (&key
    ((:sum __sum) 0)
    ((:testvalue __testvalue) 0)
    )
   (send-super :init)
   (setq _sum (round __sum))
   (setq _testvalue (round __testvalue))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:testvalue
   (&optional __testvalue)
   (if __testvalue (setq _testvalue __testvalue)) _testvalue)
  (:serialization-length
   ()
   (+
    ;; int64 _sum
    8
    ;; int64 _testvalue
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _sum
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _sum (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _sum) (= (length (_sum . bv)) 2)) ;; bignum
              (write-long (ash (elt (_sum . bv) 0) 0) s)
              (write-long (ash (elt (_sum . bv) 1) -1) s))
             ((and (class _sum) (= (length (_sum . bv)) 1)) ;; big1
              (write-long (elt (_sum . bv) 0) s)
              (write-long (if (>= _sum 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _sum s)(write-long (if (>= _sum 0) 0 #xffffffff) s)))
     ;; int64 _testvalue
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _testvalue (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _testvalue) (= (length (_testvalue . bv)) 2)) ;; bignum
              (write-long (ash (elt (_testvalue . bv) 0) 0) s)
              (write-long (ash (elt (_testvalue . bv) 1) -1) s))
             ((and (class _testvalue) (= (length (_testvalue . bv)) 1)) ;; big1
              (write-long (elt (_testvalue . bv) 0) s)
              (write-long (if (>= _testvalue 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _testvalue s)(write-long (if (>= _testvalue 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _sum
#+(or :alpha :irix6 :x86_64)
      (setf _sum (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _sum (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _testvalue
#+(or :alpha :irix6 :x86_64)
      (setf _testvalue (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _testvalue (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass ros_basics_turorials::AddTwoInts
  :super ros::object
  :slots ())

(setf (get ros_basics_turorials::AddTwoInts :md5sum-) "aa1aa1352f5bcf43b9b6f23761f75fd6")
(setf (get ros_basics_turorials::AddTwoInts :datatype-) "ros_basics_turorials/AddTwoInts")
(setf (get ros_basics_turorials::AddTwoInts :request) ros_basics_turorials::AddTwoIntsRequest)
(setf (get ros_basics_turorials::AddTwoInts :response) ros_basics_turorials::AddTwoIntsResponse)

(defmethod ros_basics_turorials::AddTwoIntsRequest
  (:response () (instance ros_basics_turorials::AddTwoIntsResponse :init)))

(setf (get ros_basics_turorials::AddTwoIntsRequest :md5sum-) "aa1aa1352f5bcf43b9b6f23761f75fd6")
(setf (get ros_basics_turorials::AddTwoIntsRequest :datatype-) "ros_basics_turorials/AddTwoIntsRequest")
(setf (get ros_basics_turorials::AddTwoIntsRequest :definition-)
      "int64 a
int64 b
---
int64 sum
int64 testvalue
")

(setf (get ros_basics_turorials::AddTwoIntsResponse :md5sum-) "aa1aa1352f5bcf43b9b6f23761f75fd6")
(setf (get ros_basics_turorials::AddTwoIntsResponse :datatype-) "ros_basics_turorials/AddTwoIntsResponse")
(setf (get ros_basics_turorials::AddTwoIntsResponse :definition-)
      "int64 a
int64 b
---
int64 sum
int64 testvalue
")



(provide :ros_basics_turorials/AddTwoInts "aa1aa1352f5bcf43b9b6f23761f75fd6")


