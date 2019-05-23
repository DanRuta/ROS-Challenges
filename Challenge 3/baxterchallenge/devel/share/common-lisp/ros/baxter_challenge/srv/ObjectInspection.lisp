; Auto-generated. Do not edit!


(cl:in-package baxter_challenge-srv)


;//! \htmlinclude ObjectInspection-request.msg.html

(cl:defclass <ObjectInspection-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ObjectInspection-request (<ObjectInspection-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectInspection-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectInspection-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name baxter_challenge-srv:<ObjectInspection-request> is deprecated: use baxter_challenge-srv:ObjectInspection-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectInspection-request>) ostream)
  "Serializes a message object of type '<ObjectInspection-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectInspection-request>) istream)
  "Deserializes a message object of type '<ObjectInspection-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectInspection-request>)))
  "Returns string type for a service object of type '<ObjectInspection-request>"
  "baxter_challenge/ObjectInspectionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectInspection-request)))
  "Returns string type for a service object of type 'ObjectInspection-request"
  "baxter_challenge/ObjectInspectionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectInspection-request>)))
  "Returns md5sum for a message object of type '<ObjectInspection-request>"
  "b7b93667ab19d45333d9d3fab6d6a1fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectInspection-request)))
  "Returns md5sum for a message object of type 'ObjectInspection-request"
  "b7b93667ab19d45333d9d3fab6d6a1fb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectInspection-request>)))
  "Returns full string definition for message of type '<ObjectInspection-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectInspection-request)))
  "Returns full string definition for message of type 'ObjectInspection-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectInspection-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectInspection-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectInspection-request
))
;//! \htmlinclude ObjectInspection-response.msg.html

(cl:defclass <ObjectInspection-response> (roslisp-msg-protocol:ros-message)
  ((colour
    :reader colour
    :initarg :colour
    :type cl:string
    :initform ""))
)

(cl:defclass ObjectInspection-response (<ObjectInspection-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectInspection-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectInspection-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name baxter_challenge-srv:<ObjectInspection-response> is deprecated: use baxter_challenge-srv:ObjectInspection-response instead.")))

(cl:ensure-generic-function 'colour-val :lambda-list '(m))
(cl:defmethod colour-val ((m <ObjectInspection-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader baxter_challenge-srv:colour-val is deprecated.  Use baxter_challenge-srv:colour instead.")
  (colour m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectInspection-response>) ostream)
  "Serializes a message object of type '<ObjectInspection-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'colour))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'colour))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectInspection-response>) istream)
  "Deserializes a message object of type '<ObjectInspection-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'colour) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'colour) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectInspection-response>)))
  "Returns string type for a service object of type '<ObjectInspection-response>"
  "baxter_challenge/ObjectInspectionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectInspection-response)))
  "Returns string type for a service object of type 'ObjectInspection-response"
  "baxter_challenge/ObjectInspectionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectInspection-response>)))
  "Returns md5sum for a message object of type '<ObjectInspection-response>"
  "b7b93667ab19d45333d9d3fab6d6a1fb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectInspection-response)))
  "Returns md5sum for a message object of type 'ObjectInspection-response"
  "b7b93667ab19d45333d9d3fab6d6a1fb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectInspection-response>)))
  "Returns full string definition for message of type '<ObjectInspection-response>"
  (cl:format cl:nil "string colour~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectInspection-response)))
  "Returns full string definition for message of type 'ObjectInspection-response"
  (cl:format cl:nil "string colour~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectInspection-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'colour))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectInspection-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectInspection-response
    (cl:cons ':colour (colour msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ObjectInspection)))
  'ObjectInspection-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ObjectInspection)))
  'ObjectInspection-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectInspection)))
  "Returns string type for a service object of type '<ObjectInspection>"
  "baxter_challenge/ObjectInspection")