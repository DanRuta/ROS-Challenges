;; Auto-generated. Do not edit!


(when (boundp 'baxter_challenge::ObjectInspection)
  (if (not (find-package "BAXTER_CHALLENGE"))
    (make-package "BAXTER_CHALLENGE"))
  (shadow 'ObjectInspection (find-package "BAXTER_CHALLENGE")))
(unless (find-package "BAXTER_CHALLENGE::OBJECTINSPECTION")
  (make-package "BAXTER_CHALLENGE::OBJECTINSPECTION"))
(unless (find-package "BAXTER_CHALLENGE::OBJECTINSPECTIONREQUEST")
  (make-package "BAXTER_CHALLENGE::OBJECTINSPECTIONREQUEST"))
(unless (find-package "BAXTER_CHALLENGE::OBJECTINSPECTIONRESPONSE")
  (make-package "BAXTER_CHALLENGE::OBJECTINSPECTIONRESPONSE"))

(in-package "ROS")





(defclass baxter_challenge::ObjectInspectionRequest
  :super ros::object
  :slots ())

(defmethod baxter_challenge::ObjectInspectionRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass baxter_challenge::ObjectInspectionResponse
  :super ros::object
  :slots (_colour ))

(defmethod baxter_challenge::ObjectInspectionResponse
  (:init
   (&key
    ((:colour __colour) "")
    )
   (send-super :init)
   (setq _colour (string __colour))
   self)
  (:colour
   (&optional __colour)
   (if __colour (setq _colour __colour)) _colour)
  (:serialization-length
   ()
   (+
    ;; string _colour
    4 (length _colour)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _colour
       (write-long (length _colour) s) (princ _colour s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _colour
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _colour (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass baxter_challenge::ObjectInspection
  :super ros::object
  :slots ())

(setf (get baxter_challenge::ObjectInspection :md5sum-) "b7b93667ab19d45333d9d3fab6d6a1fb")
(setf (get baxter_challenge::ObjectInspection :datatype-) "baxter_challenge/ObjectInspection")
(setf (get baxter_challenge::ObjectInspection :request) baxter_challenge::ObjectInspectionRequest)
(setf (get baxter_challenge::ObjectInspection :response) baxter_challenge::ObjectInspectionResponse)

(defmethod baxter_challenge::ObjectInspectionRequest
  (:response () (instance baxter_challenge::ObjectInspectionResponse :init)))

(setf (get baxter_challenge::ObjectInspectionRequest :md5sum-) "b7b93667ab19d45333d9d3fab6d6a1fb")
(setf (get baxter_challenge::ObjectInspectionRequest :datatype-) "baxter_challenge/ObjectInspectionRequest")
(setf (get baxter_challenge::ObjectInspectionRequest :definition-)
      "
---
string colour

")

(setf (get baxter_challenge::ObjectInspectionResponse :md5sum-) "b7b93667ab19d45333d9d3fab6d6a1fb")
(setf (get baxter_challenge::ObjectInspectionResponse :datatype-) "baxter_challenge/ObjectInspectionResponse")
(setf (get baxter_challenge::ObjectInspectionResponse :definition-)
      "
---
string colour

")



(provide :baxter_challenge/ObjectInspection "b7b93667ab19d45333d9d3fab6d6a1fb")


