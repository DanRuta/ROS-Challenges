
(cl:in-package :asdf)

(defsystem "baxter_challenge-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "BlockState" :depends-on ("_package_BlockState"))
    (:file "_package_BlockState" :depends-on ("_package"))
  ))