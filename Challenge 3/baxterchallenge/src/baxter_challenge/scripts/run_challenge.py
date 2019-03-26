#!/usr/bin/env python

import sys
from copy import deepcopy

import numpy as np
import rospy

from helper import *
from arm_controller import ArmController

class PickAndPlace:
    def __init__(self):
        """
        Setup Baxter and the surrounding environment
        """
        print("========= Initialise pick and place system =========")
        self.grasping_arm = ArmController("left")
        self.non_grasping_arm = ArmController("right")

        self.poses = create_poses()

    def pick(self):

        print("========= Pick object =========")
        print("Open grippers")
        self.grasping_arm.gripper.open(True)

        print("Move above object")
        target_pose = deepcopy(self.poses["object"])
        target_pose.position.z += 0.3
        self.grasping_arm.move_arm(target_pose)

        print("Grasp object")
        target_pose = deepcopy(self.poses["object"])
        self.grasping_arm.move_arm(target_pose)
        self.grasping_arm.gripper.close(True)

        print("Lift object")
        target_pose = deepcopy(self.poses["object"])
        target_pose.position.z += 0.3
        self.grasping_arm.move_arm(target_pose)

    def place(self):
        print("========= Inspect object =========")
        target_pose = deepcopy(self.poses["inspect"])
        self.grasping_arm.move_arm(target_pose)

        print("Determine object colour")
        object_colour = inspect_object()
        print("Detected_colour: {}".format(object_colour))

        print("========= Place object =========")
        print("Move to above bin")
        target_pose = deepcopy(self.poses["tote_{}".format(object_colour)])
        target_pose.position.z += 0.3
        self.grasping_arm.move_arm(target_pose)

        print("Place object in bin")
        target_pose = deepcopy(self.poses["tote_{}".format(object_colour)])
        self.grasping_arm.move_arm(target_pose)
        self.grasping_arm.gripper.open(True)

        print("Move back to neutral position")
        target_pose = deepcopy(self.poses["tote_{}".format(object_colour)])
        target_pose.position.z += 0.3
        self.grasping_arm.move_arm(target_pose)
        self.grasping_arm.reset_arm()

        return object_colour


if __name__=="__main__":
    rospy.init_node('baxter_challenge', anonymous=True)

    sim = rospy.get_param('~sim')
    max_attempts = rospy.get_param('~max_attempts', -1)
    attempts = 0

    # Load Gazebo environment with table and totes
    if sim:
         env = GazeboEnvironment()
         env.load_gazebo_environment()

    # Initialise pick and place controller 
    controller = PickAndPlace()

    # Start pick and place loop
    while not rospy.is_shutdown():

        if max_attempts is -1:
            option = raw_input("Press enter to attempt pick and place (or enter q to quit):")
            if option == "q":
                break
        elif attempts >= max_attempts:
            break
        
        # Delete old block and load new block
        if sim:
            env.delete_gazebo_object_models()
            env.load_gazebo_object()
            
        # Attempt pick and place
        controller.pick()
        detected_colour = controller.place()
        
        # Publish results of pick and place (USED FOR MARKING!)
        if sim:
            env.publish_results(detected_colour)

        attempts = attempts + 1
    
    # Delete block and other objects in Gazebo envrionment when finished
    if sim:
        env.delete_gazebo_object_models()
        env.delete_gazebo_env_models()