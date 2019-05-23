; Auto-generated. Do not edit!


(cl:in-package baxter_challenge-msg)


;//! \htmlinclude BlockState.msg.html

(cl:defclass <BlockState> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (block_colour
    :reader block_colour
    :initarg :block_colour
    :type cl:string
    :initform "")
   (detected_colour
    :reader detected_colour
    :initarg :detected_colour
    :type cl:string
    :initform ""))
)

(cl:defclass BlockState (<BlockState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BlockState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BlockState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name baxter_challenge-msg:<BlockState> is deprecated: use baxter_challenge-msg:BlockState instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <BlockState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader baxter_challenge-msg:pose-val is deprecated.  Use baxter_challenge-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'block_colour-val :lambda-list '(m))
(cl:defmethod block_colour-val ((m <BlockState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader baxter_challenge-msg:block_colour-val is deprecated.  Use baxter_challenge-msg:block_colour instead.")
  (block_colour m))

(cl:ensure-generic-function 'detected_colour-val :lambda-list '(m))
(cl:defmethod detected_colour-val ((m <BlockState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader baxter_challenge-msg:detected_colour-val is deprecated.  Use baxter_challenge-msg:detected_colour instead.")
  (detected_colour m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BlockState>) ostream)
  "Serializes a message object of type '<BlockState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'block_colour))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'block_colour))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'detected_colour))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'detected_colour))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BlockState>) istream)
  "Deserializes a message object of type '<BlockState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'block_colour) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'block_colour) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'detected_colour) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'detected_colour) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BlockState>)))
  "Returns string type for a message object of type '<BlockState>"
  "baxter_challenge/BlockState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BlockState)))
  "Returns string type for a message object of type 'BlockState"
  "baxter_challenge/BlockState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BlockState>)))
  "Returns md5sum for a message object of type '<BlockState>"
  "64375395e16156e7524bad1bd00751b2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BlockState)))
  "Returns md5sum for a message object of type 'BlockState"
  "64375395e16156e7524bad1bd00751b2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BlockState>)))
  "Returns full string definition for message of type '<BlockState>"
  (cl:format cl:nil "geometry_msgs/Pose pose~%string block_colour~%string detected_colour~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BlockState)))
  "Returns full string definition for message of type 'BlockState"
  (cl:format cl:nil "geometry_msgs/Pose pose~%string block_colour~%string detected_colour~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BlockState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     4 (cl:length (cl:slot-value msg 'block_colour))
     4 (cl:length (cl:slot-value msg 'detected_colour))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BlockState>))
  "Converts a ROS message object to a list"
  (cl:list 'BlockState
    (cl:cons ':pose (pose msg))
    (cl:cons ':block_colour (block_colour msg))
    (cl:cons ':detected_colour (detected_colour msg))
))
