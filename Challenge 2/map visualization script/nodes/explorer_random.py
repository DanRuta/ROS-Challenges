#!/usr/bin/env python
from __future__ import print_function

import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped

from explorer_base import Explorer

import os

logFile = "/user/HS122/dr00392/chall2/src/turtlebot_explorer/nodes/outFile.txt"

print("=================== explorer_random.py")

class RandomExplorer(Explorer):

    def __init__(self):

        print("new RandomExplorer explorer_random.py")

        with open(logFile, "a") as file:
            file.write("new RandomExplorer explorer_random_services.py\n")

        # Define a Subscriber for the Map
        self.map_sub = rospy.Subscriber("map", OccupancyGrid, self.map_cb)

        # Define a Timer to send goals
        # rospy.Timer(rospy.Duration(5), self.timer_cb)
        rospy.Timer(rospy.Duration(1), self.timer_cb)

        # Define a Simple Goal Publisher
        self.goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

    # Timer Callback Checks map exists and calls processor
    def timer_cb(self, event):
        rospy.loginfo("Timer Callback!")

        if self.latest_map_msg is not None:
            goal_msg = self.process_map()
            self.send_goal(goal_msg)

        else:
            rospy.logwarn("No Map! Can't find goal!")

    # Map is published after every update, which triggers us to update our local copy.
    def map_cb(self, msg):

        with open(logFile, "a") as file:
            file.write("Got a map (RandomExplorer)\n")

        rospy.loginfo("Got a map!")
        self.update_map(msg)

    # Overload get_goal to select Random Valid Cell
    def get_goal(self, cells_to_pick, map_origin, res):
        # Pick Cell
        rand_idx = np.random.randint(0, len(cells_to_pick))

        goal = cells_to_pick[rand_idx]
        goal = (goal * res) + map_origin
        return goal

    # Overload get_valid_cells to return explored cells
    def get_valid_cells(self, height, gridmap, width):
        # Get Number of Explored Cells
        cells_explored = np.count_nonzero(gridmap > -1)
        rospy.loginfo("Cells Explored %i", cells_explored)

        # Create an Array with Cells to Pick
        cells = 0
        cells_to_pick = np.zeros((cells_explored, 2))
        for y in xrange(0, height):
            for x in xrange(0, width):
                idx = x + y * width
                if gridmap[idx] > -1:
                    #if self.check_cell_region(gridmap, x, y, width):
                    cells_to_pick[cells][0] = x
                    cells_to_pick[cells][1] = y
                    cells = cells + 1

        return cells_to_pick

    # Send Goal as Simple Message (no feedback)
    def send_goal(self, goal):
        self.goal_pub.publish(goal)


if __name__ == '__main__':
    rospy.init_node('random_explorer',anonymous=True)
    explorer = RandomExplorer()
    explorer.loop()
