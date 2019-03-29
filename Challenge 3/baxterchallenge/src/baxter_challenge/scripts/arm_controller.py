#!/usr/bin/env python

import sys
from copy import deepcopy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np
from control_msgs.msg import FollowJointTrajectoryActionResult
from baxter_interface import gripper

from geometry_msgs.msg import PoseStamped

from helper import *

NEUTRAL_JOINT_POSITIONS = {"left": [1.15, -0.98, -0.25, 1.42, 0.14, 1.09, 0.29],
                           "right": [-1.15, -0.98, 0.25, 1.42, -0.14, 1.09, -0.29]}

#NEUTRAL_JOINT_POSITIONS = {'left':  [0.60, 0.08, -1.56, 1.0,  0.02, 1.61, 1.57],
#                           'right':  [-0.60, 0.08, 1.56, 1.0,  -0.02, 1.61, -1.57]}

class ArmController:
    def __init__(self, arm="left"):
        """
        Setup Baxter and the surrounding environment
        """
        # First initialize moveit_commander.
        moveit_commander.roscpp_initialize(sys.argv)
        self.arm = arm
        self.robot = moveit_commander.RobotCommander()

        # Add table to moveit scene
        self.scene = moveit_commander.PlanningSceneInterface()
        rospy.sleep(2)
        p = PoseStamped()
        p.header.frame_id = self.robot.get_planning_frame()
        p.pose.position.x = 0.7
        p.pose.position.y = 0.0
        p.pose.position.z = 0.35
        self.scene.add_box("table", p, (0.9, 1.8, 0.7))

        # Add tote_red to moveit scene
        self.scene = moveit_commander.PlanningSceneInterface()
        rospy.sleep(2)
        p1 = PoseStamped()
        p1.header.frame_id = self.robot.get_planning_frame()
        p1.pose.position.x = 0.6
        p1.pose.position.y = 0.1
        p1.pose.position.z = 0.75
        self.scene.add_box("tote_red", p1, (0.6, 0.35, 0.075))

        # Add tote_red to moveit scene
        self.scene = moveit_commander.PlanningSceneInterface()
        rospy.sleep(2)
        p2 = PoseStamped()
        p2.header.frame_id = self.robot.get_planning_frame()
        p2.pose.position.x = 0.6
        p2.pose.position.y = 0.3
        p2.pose.position.z = 0.75
        self.scene.add_box("tote_blue", p2, (0.6, 0.35, 0.075))

        # Initialize moveit arm controller and gripper
        self.moveit_arm = moveit_commander.MoveGroupCommander("{}_arm".format(arm))
        self.gripper = gripper.Gripper(arm)
        self.gripper.calibrate()

        # Create this DisplayTrajectory publisher which is used below to publish trajectories for RVIZ to visualize.
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                            moveit_msgs.msg.DisplayTrajectory,
                                                            queue_size=10)

        # Subscribe to joint trajectory result to get feedback about moves
        self.move_number_executed = None
        self.move_error_code = 0
        self.move_error_string = None
        rospy.Subscriber("/robot/limb/{}/follow_joint_trajectory/result".format(arm),
                         FollowJointTrajectoryActionResult,
                         self.result_callback)

        # Move arm to safe position
        self.reset_arm()

    def result_callback(self, data):
        self.move_number_executed = data.header.seq
        self.move_error_code = data.result.error_code
        self.move_error_string = data.result.error_string

    def get_current_pose(self):
        return self.moveit_arm.get_current_pose().pose

    def reset_arm(self):
        self.gripper.open(True)
        self.move_arm(NEUTRAL_JOINT_POSITIONS[self.arm])

    def move_arm(self, target, execute=True):
        print("Generating arm plan for target: {}".format(target))

        # HINT 2: What planning settings is MoveIt using?
        # These are the planner settings: default RRT configuration

        self.moveit_arm.set_goal_tolerance(0.0005) # 0.0005

        #I tried a different planner configuration but it doesn't make a difference
        self.moveit_arm.set_planner_id("RRTstarkConfigDefault")
        #self.moveit_arm.set_planner_id("RRTConnectkConfigDefault")
        if type(target) == geometry_msgs.msg.Pose:
            self.moveit_arm.set_pose_target(target)
        elif type(target) == list:
            self.moveit_arm.set_joint_value_target(target)
        self.moveit_arm.set_planning_time(5.0) # 3.0
        grasping_arm_plan = self.moveit_arm.plan()
        rospy.sleep(0.1)

        # Execute the movement
        if execute and len(grasping_arm_plan.joint_trajectory.points) > 0:
            print("Executing plans")
            self.moveit_arm.execute(grasping_arm_plan)
            rospy.sleep(0.1)
            return True
        elif len(grasping_arm_plan.joint_trajectory.points) == 0:
            print("Failed to find a plan - check target goal")
            return False
        else:
            print("Not executing plan")
            return True
