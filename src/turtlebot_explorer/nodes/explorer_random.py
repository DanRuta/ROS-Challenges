#!/usr/bin/env python
from __future__ import print_function

import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import Odometry
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

    def get_myPos(self, map_origin, res):
        myPos = rospy.wait_for_message("/odom", Odometry)
        #rospy.loginfo("####################################YAY! I found me!")
        #rospy.loginfo(str(myPos.pose.pose.position))
        myX = myPos.pose.pose.position.x
        myY = myPos.pose.pose.position.y
        #rospy.loginfo("######################################## in X & Y!")
        #rospy.loginfo(str(myX))
        #rospy.loginfo(str(myY))
        myPosXY = [myX, myY]
        #rospy.loginfo("######################################## MAP Origin!")
        #rospy.loginfo(str(map_origin))
        myIdx = np.floor((myPosXY - map_origin)/res)
        myIdx = [int(myIdx[0]), int(myIdx[1])]
        #rospy.loginfo("######################################## Pos in Indices!")
        #rospy.loginfo(str(myIdx))
        return myIdx

    # Overload get_goal to select Random Valid Cell
    def get_goal(self, cells_to_pick, map_origin, res):
        # Pick Cell
        # Randomly Select a frontier cell
        # cells_to_pick_merged = np.sum(cells_to_pick, axis=1)
        # cells_nonzero = np.count_nonzero(cells_to_pick_merged > 0)
        # rospy.loginfo("Cells nonzero %i", cells_nonzero)
        # #rand_idx = np.random.randint(0, len(cells_to_pick))
        # rand_idx = np.random.randint(0, cells_nonzero)
        # goal = cells_to_pick[rand_idx]

        # find the nearest frontier medianfrontierPoints
        robotPos = self.get_myPos(map_origin, res)
        goal = self.pickMove(robotPos, cells_to_pick)

        self.prevGoal = goal
        rospy.loginfo("=======================")
        rospy.loginfo(str(goal))
        goal = (goal * res) + map_origin
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

        for y in xrange(0, height):
            for x in xrange(0, width):
                idx = x + y * width
                if self.is_boundary(gridmap, idx, width):
                    #if gridmap[idx] > -1 and gridmap[idx] < mn:
                    #if gridmap[idx] > -1:
                    #if self.check_cell_region(gridmap, x, y, width):
                    cells_to_pick[cells][0] = x
                    cells_to_pick[cells][1] = y
                    cells = cells + 1
        cells_to_pick = np.resize(cells_to_pick,(cells,2))
        return cells_to_pick

    def is_boundary(self, gridmap, idx, width):

        if gridmap[idx] == 0 and (gridmap[idx-width-1] == -1 or gridmap[idx-width] == -1 or gridmap[idx-width+1] == -1 or gridmap[idx-1] == -1 or gridmap[idx+1] == -1 or gridmap[idx+width-1] == -1 or gridmap[idx+width] == -1 or gridmap[idx+width+1] == -1):
            bool = True
        else:
            bool = False

        return bool

    # Get the means, size of frontier, and Euclidean distance to the mean
    def getFrontierData(self, robotPos, frontierPoints):

        groups = self.groupFrontiers(frontierPoints)
        means = []
        sizes = []
        distances = []

        for group in groups:

            mean = [0, 0]

            for [x,y] in group:
                mean[0] += x
                mean[1] += y

            mean[0] /= len(group)
            mean[1] /= len(group)
            means.append(mean)
            sizes.append(len(group))
            distances.append(sqrt((mean[0]-robotPos[0])**2, (mean[1]-robotPos[1])**2))

        return means, sizes, distances

    # Return the x,y coordinates to the closest median point along the grouped up frontiers
    def pickMove(self, robotPos, frontierPoints):
        rospy.loginfo("=======================1")
        groups = self.groupFrontiers(frontierPoints)
        distances = []
        medians = []
        shortestDistanceGroup = 0
        shortestDistance = 100000

        for g in range(len(groups)):
            median = groups[g][np.floor(len(groups[g])/2)]
            euclideanToMedian = np.sqrt((median[0]-robotPos[0])**2, (median[1]-robotPos[1])**2)
            distances.append(euclideanToMedian)

            if euclideanToMedian < shortestDistance:
                shortestDistance = euclideanToMedian
                shortestDistanceGroup = g
        return medians[shortestDistanceGroup]

    # Get a list of grouped up frontier points
    def groupFrontiers(self, frontierPoints):
        # [[1,2], [1,2], [1,2]]

        THRESHOLD = 1

        # A 2D array, of grouped up points
        groups = [[frontierPoints[0]]]
        # rospy.loginfo("=======================")
        # rospy.loginfo(groups)
        # Loop through all the frontier points, except the first
        # for [x,y] in range(1, len(frontierPoints)):
        for nCells in range(1, len(frontierPoints)):
            x = frontierPoints[nCells][0]
            y = frontierPoints[nCells][1]
            # Loop through every group, and check if this point is within
            # 1, in both x and y of every point, and assign this point to the group,
            # else create a new group, and assign this point, as the first in the group
            groupFound = False
            for g in range(len(groups)):
                for [x2,y2] in groups[g]:
                    # rospy.loginfo("=======================4")
                    # If the two points are at most at corners, to each other, they are adjacent
                    # (Euclidean distance)
                    if np.sqrt((x2-x)**2 + (y2-y)**2) <= THRESHOLD and not groupFound:
                    # They are adjacent, so add them to this group
                        groups[g].append([x,y])
                        groupFound = True

            # No group has points that are near this point, so create a new group
            # So make a new group, and add this point to it
            if not groupFound:
                groups.append([[x,y]])
            rospy.loginfo("=======================3")
        rospy.loginfo("=======================2")
        return groups


    # Send Goal as Simple Message (no feedback)
    def send_goal(self, goal):
        self.goal_pub.publish(goal)


if __name__ == '__main__':
    rospy.init_node('random_explorer',anonymous=True)
    explorer = RandomExplorer()
    explorer.loop()
