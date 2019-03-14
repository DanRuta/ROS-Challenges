#!/usr/bin/env python
from __future__ import print_function

import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped

import cv2

from explorer_base import Explorer

class RandomExplorer(Explorer):

    prevGoal = None

    def __init__(self):

        # Define a Subscriber for the Map
        self.map_sub = rospy.Subscriber("map", OccupancyGrid, self.map_cb)

        # Define a Timer to send goals
        rospy.Timer(rospy.Duration(5), self.timer_cb)

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
        rospy.loginfo("Got a map!")
        self.update_map(msg)

    # Overload get_goal to select Random Valid Cell
    def get_goal(self, cells_to_pick, map_origin, res):
        # Pick Cell

        cells_nonzero = np.count_nonzero(cells_to_pick > 0)
        rospy.loginfo("Cells nonzero %i", cells_nonzero)

        #rand_idx = np.random.randint(0, len(cells_to_pick))
        rand_idx = np.random.randint(0, cells_nonzero)


        goal = cells_to_pick[rand_idx]
        goal = (goal * res) + map_origin
        self.prevGoal = goal
        return goal

    # Overload get_valid_cells to return explored cells
    def get_valid_cells(self, height, gridmap, width):

        #My extra code

        gridmap_positive = gridmap[gridmap > -1]
        mn = np.mean(gridmap_positive)
        mx = np.max(gridmap_positive)
        cells_positive = np.count_nonzero(gridmap_positive < mn)

        # Get Number of Explored Cells

        cells_explored = np.count_nonzero(gridmap > -1)

        rospy.loginfo("Cells Explored %i", cells_explored)
        rospy.loginfo("Mean value is %d", mn)
        rospy.loginfo("Max value is %d", mx)
        rospy.loginfo("Cells Positive %i", cells_positive)

        # Create an Array with Cells to Pick
        cells = 0
        cells_to_pick = np.zeros((cells_explored, 2))
        #cells_to_pick = np.zeros((cells_positive, 2))
        # if prevGoal is None:
            for y in xrange(0, height):
                for x in xrange(0, width):
                    idx = x + y * width
                    if gridmap[idx] == 0 and (gridmap[idx-width-1] == -1 or gridmap[idx-width] == -1 or gridmap[idx-width+1] == -1 or gridmap[idx-1] == -1 or gridmap[idx+1] == -1 or gridmap[idx+width-1] == -1 or gridmap[idx+width] == -1 or gridmap[idx+width+1] == -1):
                        #if gridmap[idx] > -1 and gridmap[idx] < mn:
                        #if gridmap[idx] > -1:
                        #if self.check_cell_region(gridmap, x, y, width):
                        cells_to_pick[cells][0] = x
                        cells_to_pick[cells][1] = y
                        cells = cells + 1
        # else:
            # for between this shit


        return cells_to_pick



    # Send Goal as Simple Message (no feedback)
    def send_goal(self, goal):
        self.goal_pub.publish(goal)


if __name__ == '__main__':
    rospy.init_node('random_explorer',anonymous=True)
    explorer = RandomExplorer()
    explorer.loop()
