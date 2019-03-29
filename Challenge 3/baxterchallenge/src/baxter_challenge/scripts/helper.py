import argparse
import struct
import sys
import copy
import numpy as np

import rospy
import rospkg

from gazebo_msgs.srv import (
    SpawnModel,
    DeleteModel,
    GetModelState,
    GetModelProperties
)
from geometry_msgs.msg import (
    Pose,
    Point,
    Quaternion)

from baxter_challenge.msg import BlockState

from baxter_challenge.srv import ObjectInspection


def inspect_object():
    """
    Connect to inspect object service and get the detected object colour
    """
    rospy.wait_for_service('inspect_object')
    try:
        inspect_object_srv = rospy.ServiceProxy('inspect_object', ObjectInspection)
        resp = inspect_object_srv()
        return resp.colour
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e


def create_poses():
    """
    Return set of posed which determine the positions used for the pick and place sequence
    """
    poses = {"object": Pose(position=Point(x=0.6, y=0.6, z=0.75), orientation=Quaternion(x=0, y=1, z=0, w=0)), 	#Where the object is
             "inspect": Pose(position=Point(x=0.5, y=0.0, z=1.6), orientation=Quaternion(x=0, y=0, z=0, w=1)), 		#Where the camera is
             "tote_red": Pose(position=Point(x=0.6, y=-0.1, z=0.85), orientation=Quaternion(x=0, y=1, z=0, w=0)), 	#Where the red box is
             "tote_blue": Pose(position=Point(x=0.6, y=0.3, z=0.85), orientation=Quaternion(x=0, y=1, z=0, w=0))} 	#Where the blue box is
             # originally z = 0.75 for tote poses z
    return poses


class GazeboEnvironment():
    def __init__(self):
        """
        Creates service calls and publisher for managing the Baxter gazebo environment
        """
        # Set up gazebo services for spawning, deleting and inspecting models
        rospy.wait_for_service('/gazebo/spawn_sdf_model')
        self.spawn_sdf = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        rospy.wait_for_service('/gazebo/spawn_urdf_model')
        self.spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
        rospy.wait_for_service('/gazebo/delete_model')
        self.delete_model = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel)
        rospy.wait_for_service('/gazebo/get_model_state')
        self.get_model_state = rospy.ServiceProxy( '/gazebo/get_model_state', GetModelState)

        # Set the path to the models
        self.model_path = rospkg.RosPack().get_path('baxter_challenge') + "/models/"

        # Create publisher for the result of pick and place attempts in Gazebo
        self.block_state_pub = rospy.Publisher('block_state', BlockState)
        self.block_colour = None

    def load_gazebo_environment(self,
                                table_pose=Pose(position=Point(x=0.7, y=0.4565, z=-0.04)), table_reference_frame="world",
                                tote_pose=Pose(position=Point(x=0.6, y=-0.1, z=0.735)), tote_reference_frame="world"):
        """
        Load the tables and the totes for Baxter pick and place challenge
        """
        # Load table SDF
        table_xml = ''
        with open(self.model_path + "cafe_table/model.sdf", "r") as table_file:
            table_xml = table_file.read().replace('\n', '')
        # Spawn table SDF
        rospy.wait_for_service('/gazebo/spawn_sdf_model')
        try:
            self.spawn_sdf("cafe_table_1", table_xml, "/", table_pose, table_reference_frame)
            table_pose.position.y = -table_pose.position.y
            self.spawn_sdf("cafe_table_2", table_xml, "/", table_pose, table_reference_frame)
        except rospy.ServiceException, e:
            rospy.logerr("Spawn SDF service call failed: {0}".format(e))

        # Load tote SDF
        red_tote_xml = ''
        blue_tote_xml = ''
        with open(self.model_path + "tote/red_model.sdf", "r") as table_file:
            red_tote_xml = table_file.read().replace('\n', '')
        with open(self.model_path + "tote/blue_model.sdf", "r") as table_file:
            blue_tote_xml = table_file.read().replace('\n', '')
        # Spawn tote SDF
        try:
            self.spawn_sdf("tote_1", red_tote_xml, "/", tote_pose, tote_reference_frame)
            tote_pose.position.y = tote_pose.position.y + 0.4
            self.spawn_sdf("tote_2", blue_tote_xml, "/", tote_pose, tote_reference_frame)
        except rospy.ServiceException, e:
            rospy.logerr("Spawn SDF service call failed: {0}".format(e))

    def load_gazebo_object(self, block_pose=Pose(position=Point(x=0.6, y=0.6, z=0.735)), block_reference_frame="world"):
        """
        Load a block of randomly chosen colour for Baxter pick and place challenge
        """
        self.block_colour = np.random.choice(["red", "blue"])
        # Load block URDF
        block_xml = ''
        with open(self.model_path + "block/{}_model.urdf".format(self.block_colour), "r") as block_file:
            block_xml = block_file.read().replace('\n', '')
        # Spawn block URDF
        try:
            self.spawn_urdf = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
            self.spawn_urdf("block", block_xml, "/", block_pose, block_reference_frame)
        except rospy.ServiceException, e:
            rospy.logerr("Spawn URDF service call failed: {0}".format(e))

    def publish_results(self, detected_colour=None):
        """
        Publish results of a pick and place attempt including the true object colour, position and the detected colour
        """
        try:
            block_state = BlockState()
            block_state.pose = self.get_model_state("block", "").pose
            block_state.block_colour = self.block_colour
            block_state.detected_colour = detected_colour

            self.block_state_pub.publish(block_state)
        except rospy.ServiceException, e:
            rospy.logerr("Get model state service call failed: {0}".format(e))

    def delete_gazebo_env_models(self):
        """
        Delete Gazebo environment models - tables and totes
        """
        try:
            self.delete_model("cafe_table_1")
            self.delete_model("cafe_table_2")
            self.delete_model("tote_1")
            self.delete_model("tote_2")
        except rospy.ServiceException, e:
            rospy.loginfo("Delete Model service call failed: {0}".format(e))

    def delete_gazebo_object_models(self):
        """
        Delete Gazebo block model and reset block colour
        """
        try:
            self.delete_model("block")
            self.block_colour = None
        except rospy.ServiceException, e:
            rospy.loginfo("Delete Model service call failed: {0}".format(e))
