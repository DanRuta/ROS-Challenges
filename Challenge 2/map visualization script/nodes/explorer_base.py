from __future__ import print_function

import rospy
import numpy as np

from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped


print("=================== explorer_base.py")
logFile = "/user/HS122/dr00392/chall2/src/turtlebot_explorer/nodes/outFile.txt"
mapFile = "/user/HS122/dr00392/chall2/src/turtlebot_explorer/nodes/map.txt"

# Explorer Base Class
class Explorer:

    def __init__(self):
        rospy.loginfo("Explorer Base Class")
        self.latest_map_msg = None
        self.latest_map = None

    def update_map(self, map_msg):
        self.latest_map_msg = map_msg
        self.latest_map = np.array(self.latest_map_msg.data)
        return True

    def process_map(self):

        with open(logFile, "a") as file:
            file.write("process_map\n")

        np.savetxt(mapFile, self.latest_map)

        # print("============= 1")
        # print(self.latest_map)
        # print("============= 2")

        # with open(mapFile, "w", encoding="utf-8") as file:
        #     file.write(self.latest_map)

        # Get Map Metadata
        width = self.latest_map_msg.info.width
        height = self.latest_map_msg.info.height
        res = self.latest_map_msg.info.resolution
        map_origin = np.array([self.latest_map_msg.info.origin.position.x, self.latest_map_msg.info.origin.position.y])
        map_frame_id = self.latest_map_msg.header.frame_id
        stamp = self.latest_map_msg.header.stamp

        # Pick Goal and Crate Msg
        cells_to_pick = self.get_valid_cells(height, self.latest_map, width)
        goal = self.get_goal(cells_to_pick, map_origin, res)
        goal_msg = self.make_goal_msg(goal, map_frame_id)

        return goal_msg

    def get_valid_cells(self, height, map, width):
        cells_to_pick = np.zeros((1, 2))
        return cells_to_pick

    def get_goal(self, cells_to_pick, map_origin, res):
        goal = cells_to_pick[0]
        goal = (goal * res) + map_origin
        return goal

    def make_goal_msg(self, goal, frame_id="map"):
        # Get Message
        goal_msg = PoseStamped()
        goal_msg.pose.position.x = goal[0]
        goal_msg.pose.position.y = goal[1]
        goal_msg.pose.position.z = 0
        goal_msg.pose.orientation.x = 0
        goal_msg.pose.orientation.y = 0
        goal_msg.pose.orientation.z = 0
        goal_msg.pose.orientation.w = 1
        goal_msg.header.frame_id = frame_id
        goal_msg.header.stamp = rospy.Time.now()
        return goal_msg

    def send_goal(self, goal):
        raise NotImplementedError()

    def loop(self):
        rospy.spin()
