#!/usr/bin/env python

from baxter_challenge.srv import ObjectInspection
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2


class ObjectInspector:
    def __init__(self):
        rospy.init_node("object_inspection_service")

        self.bridge = CvBridge()
        self.cv_image = None
        self.image_set = False
        rospy.Subscriber("/cameras/head_camera/image", Image, self.image_callback)

        rospy.Service("inspect_object", ObjectInspection, self.handle_inspection_request)
        print("Ready to inspect objects")

        rospy.spin()

    def image_callback(self, data):
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            self.image_set = True
        except CvBridgeError as e:
            print(e)

    def handle_inspection_request(self, req):
        print(self.image_set)
        if self.image_set:
            print("Saving image")
            cv2.imwrite("/tmp/object_inspection.png", self.cv_image)
            self.image_set = False
        print("Choosing colour")
        # Convert to hsv
        hsv = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)
        # Mask of blue
        mask_blue = cv2.inRange(hsv, (100,150,0), (140,255,255))
        # Mask of red (need 2 as different ends of the colour wheel)
        mask1_red = cv2.inRange(hsv, (0,70,50), (10,255,255))
        mask2_red = cv2.inRange(hsv, (170,70,50), (180,255,255))
        # Final mask of red
        mask_red = cv2.bitwise_or(mask1_red, mask2_red)



        colour = np.random.choice(["red", "blue"])
        return mask_red
        # return colour


if __name__ == "__main__":
    ObjectInspector()
