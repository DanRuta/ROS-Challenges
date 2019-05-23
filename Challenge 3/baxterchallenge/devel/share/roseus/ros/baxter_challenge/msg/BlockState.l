;; Auto-generated. Do not edit!


(when (boundp 'baxter_challenge::BlockState)
  (if (not (find-package "BAXTER_CHALLENGE"))
    (make-package "BAXTER_CHALLENGE"))
  (shadow 'BlockState (find-package "BAXTER_CHALLENGE")))
(unless (find-package "BAXTER_CHALLENGE::BLOCKSTATE")
  (make-package "BAXTER_CHALLENGE::BLOCKSTATE"))

(in-package "ROS")
;;//! \htmlinclude BlockState.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass baxter_challenge::BlockState
  :super ros::object
  :slots (_pose _block_colour _detected_colour ))

(defmethod baxter_challenge::BlockState
  (:init
   (&key
    ((:pose __pose) (instance geometry_msgs::Pose :init))
    ((:block_colour __block_colour) "")
    ((:detected_colour __detected_colour) "")
    )
   (send-super :init)
   (setq _pose __pose)
   (setq _block_colour (string __block_colour))
   (setq _detected_colour (string __detected_colour))
   self)
  (:pose
   (&rest __pose)
   (if (keywordp (car __pose))
       (send* _pose __pose)
     (progn
       (if __pose (setq _pose (car __pose)))
       _pose)))
  (:block_colour
   (&optional __block_colour)
   (if __block_colour (setq _block_colour __block_colour)) _block_colour)
  (:detected_colour
   (&optional __detected_colour)
   (if __detected_colour (setq _detected_colour __detected_colour)) _detected_colour)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Pose _pose
    (send _pose :serialization-length)
    ;; string _block_colour
    4 (length _block_colour)
    ;; string _detected_colour
    4 (length _detected_colour)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Pose _pose
       (send _pose :serialize s)
     ;; string _block_colour
       (write-long (length _block_colour) s) (princ _block_colour s)
     ;; string _detected_colour
       (write-long (length _detected_colour) s) (princ _detected_colour s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Pose _pose
     (send _pose :deserialize buf ptr-) (incf ptr- (send _pose :serialization-length))
   ;; string _block_colour
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _block_colour (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _detected_colour
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _detected_colour (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get baxter_challenge::BlockState :md5sum-) "64375395e16156e7524bad1bd00751b2")
(setf (get baxter_challenge::BlockState :datatype-) "baxter_challenge/BlockState")
(setf (get baxter_challenge::BlockState :definition-)
      "geometry_msgs/Pose pose
string block_colour
string detected_colour

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :baxter_challenge/BlockState "64375395e16156e7524bad1bd00751b2")


