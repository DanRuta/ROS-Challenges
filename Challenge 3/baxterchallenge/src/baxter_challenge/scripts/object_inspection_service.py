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
        self.cv_image_roi = None
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
        print("Choosing colour")#
        # colour = np.random.choice(["red", "blue"])
        rospy.loginfo("======================== DETECTING")
        self.cv_image_roi = self.get_subimage(self.cv_image)
        colour = self.get_colour()
        rospy.loginfo("======================== DETECTED")
        rospy.loginfo(str(colour))
        return colour

    def get_subimage(self, img):
        IMG_W = 200
        IMG_H = 100
        heightStart = 250
        widthStart = 530
        image = img[heightStart:heightStart+IMG_H,widthStart:widthStart+IMG_W,:]
        print(img.shape)

        image_b = img[heightStart:heightStart+IMG_H,widthStart:widthStart+IMG_W,0]
        image_g = img[heightStart:heightStart+IMG_H,widthStart:widthStart+IMG_W,1]
        image_r = img[heightStart:heightStart+IMG_H,widthStart:widthStart+IMG_W,2]

        cv2.imwrite("~/object_inspection_crop.png", image)
        return image

    def get_colour(self):
        # masking for colours
        hsv = cv2.cvtColor(self.cv_image_roi, cv2.COLOR_BGR2HSV)  # Convert to hsv
        mask_blue = cv2.inRange(hsv, (100,150,0), (140,255,255))  # Mask of blue
        mask1_red = cv2.inRange(hsv, (0,70,50), (10,255,255))     # Mask of red (first end of colour wheel)
        mask2_red = cv2.inRange(hsv, (170,70,50), (180,255,255))  # Mask of red (first end of colour wheel)
        mask_red = cv2.bitwise_or(mask1_red, mask2_red)
        # pixel count comparison
        sum_red = 0
        sum_blue = 0
        for row in mask_blue:
            for pixel in row:
                sum_blue = sum_blue + pixel
        for row in mask_red:
            for pixel in row:
                sum_red = sum_red + pixel
        if sum_blue > sum_red:
            colour = "blue"
        else:
            colour = "red"
        return colour


if __name__ == "__main__":
    ObjectInspector()
