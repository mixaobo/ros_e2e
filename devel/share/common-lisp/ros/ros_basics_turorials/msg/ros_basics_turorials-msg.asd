
(cl:in-package :asdf)

(defsystem "ros_basics_turorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CustomMsg" :depends-on ("_package_CustomMsg"))
    (:file "_package_CustomMsg" :depends-on ("_package"))
    (:file "Localize" :depends-on ("_package_Localize"))
    (:file "_package_Localize" :depends-on ("_package"))
  ))