
(cl:in-package :asdf)

(defsystem "baxter_challenge-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ObjectInspection" :depends-on ("_package_ObjectInspection"))
    (:file "_package_ObjectInspection" :depends-on ("_package"))
  ))