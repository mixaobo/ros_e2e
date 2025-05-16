; Auto-generated. Do not edit!


(cl:in-package ros_basics_turorials-msg)


;//! \htmlinclude Localize.msg.html

(cl:defclass <Localize> (roslisp-msg-protocol:ros-message)
  ((Distance
    :reader Distance
    :initarg :Distance
    :type cl:float
    :initform 0.0)
   (AoA
    :reader AoA
    :initarg :AoA
    :type cl:float
    :initform 0.0))
)

(cl:defclass Localize (<Localize>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Localize>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Localize)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ros_basics_turorials-msg:<Localize> is deprecated: use ros_basics_turorials-msg:Localize instead.")))

(cl:ensure-generic-function 'Distance-val :lambda-list '(m))
(cl:defmethod Distance-val ((m <Localize>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_basics_turorials-msg:Distance-val is deprecated.  Use ros_basics_turorials-msg:Distance instead.")
  (Distance m))

(cl:ensure-generic-function 'AoA-val :lambda-list '(m))
(cl:defmethod AoA-val ((m <Localize>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ros_basics_turorials-msg:AoA-val is deprecated.  Use ros_basics_turorials-msg:AoA instead.")
  (AoA m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Localize>) ostream)
  "Serializes a message object of type '<Localize>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'AoA))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Localize>) istream)
  "Deserializes a message object of type '<Localize>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Distance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'AoA) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Localize>)))
  "Returns string type for a message object of type '<Localize>"
  "ros_basics_turorials/Localize")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Localize)))
  "Returns string type for a message object of type 'Localize"
  "ros_basics_turorials/Localize")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Localize>)))
  "Returns md5sum for a message object of type '<Localize>"
  "fdd62682e37010cc81e982ba74365e59")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Localize)))
  "Returns md5sum for a message object of type 'Localize"
  "fdd62682e37010cc81e982ba74365e59")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Localize>)))
  "Returns full string definition for message of type '<Localize>"
  (cl:format cl:nil "float64 Distance~%float64 AoA~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Localize)))
  "Returns full string definition for message of type 'Localize"
  (cl:format cl:nil "float64 Distance~%float64 AoA~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Localize>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Localize>))
  "Converts a ROS message object to a list"
  (cl:list 'Localize
    (cl:cons ':Distance (Distance msg))
    (cl:cons ':AoA (AoA msg))
))
