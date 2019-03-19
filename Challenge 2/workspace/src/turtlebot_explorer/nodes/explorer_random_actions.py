#!/usr/bin/env python

from __future__ import print_function

import rospy
import tf2_ros
import numpy as np
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from nav_msgs.srv import GetMap, GetMapResponse

#from move_base_msgs.msg import MoveBaseGoal
#from actionlib_msgs.msg import GoalStatus

from move_base_client import GoalSender

from explorer_random_services import RandomExplorerServices

class RandomExplorerActions(RandomExplorerServices):

    def __init__(self):

        # Define a Service for Map
        rospy.wait_for_service('/dynamic_map')
        self.get_map_srv = rospy.ServiceProxy('/dynamic_map', GetMap)

        # Define a Simple Goal Client
        self.goal_sender = GoalSender()

    def loop(self):

        while not rospy.is_shutdown():
            rospy.loginfo("New Goal...")

            if self.update_map():
                goal_msg = self.process_map()
                self.goal_sender.send_goal(goal_msg)


if __name__ == '__main__':
    rospy.init_node('random_explorer_actions')
    explorer = RandomExplorerActions()
    explorer.loop()