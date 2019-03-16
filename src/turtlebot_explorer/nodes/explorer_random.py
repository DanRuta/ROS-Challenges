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
    imStuck = False

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

        '''
        cells_nonzero = np.count_nonzero(cells_to_pick > 0)
        rospy.loginfo("Cells nonzero %i", cells_nonzero)
        cells_nonzero = cells_nonzero / 2
'''

        for gl in range(0, len(cells_to_pick)):
            rospy.loginfo("Cells in cells to pick %i: ", len(cells_to_pick))
            rand_idx = np.random.randint(0, len(cells_to_pick))
            #rand_idx = np.random.randint(0, cells_nonzero)

            goal = cells_to_pick[rand_idx]
            if self.is_good_goal(goal[0], goal[1], 5, 5, 15, 5, 5):
                self.prevGoal = goal

                rospy.loginfo("Goal X: %i: ", goal[0])
                rospy.loginfo("Goal Y: %i: ", goal[1])
                rospy.loginfo(str(type(goal)))
                rospy.loginfo(str(res))
                goal = (goal * res) + map_origin
                return goal

        self.imStuck = True
        return None

    # Overload get_valid_cells to return explored cells

    def is_good_goal(self, x, y, kernelX, kernelY, thFree, thUnknown, thWall):
        width = self.latest_map_msg.info.width

        sumFree = 0
        sumUnknown = 0
        sumWall = 0

        limitX = int(np.floor(kernelX/2))
        limitY = int(np.floor(kernelY/2))
        rospy.loginfo("--------------------GOOD GOAL-------------------------------------")
        idx = x + y * width

        for i in range(-limitX, limitX+1):
            for j in range(-limitY, limitY+1):
                #if i != 0 and j != 0:

                    id = int(idx - j * width - i)

                    if id != idx:
                        #rospy.loginfo(self.latest_map[id])
                        if self.latest_map[id] == 0:
                            sumFree = sumFree + 1
                        elif self.latest_map[id] == -1:
                            sumUnknown = sumUnknown + 1
                        #elif self.latest_map[idx] > 20:
                        else:
                            sumWall = sumWall + 1

        rospy.loginfo("sum wall %i", sumWall)
        rospy.loginfo("sum free %i", sumFree)
        rospy.loginfo("sum unknow %i", sumUnknown)
        rospy.loginfo("--------------------CLOSE GOOD GOAL-------------------------------------")
        # if sumFree > thFree and sumUnknown > thUnknown:

        if sumFree > thFree and sumUnknown > thUnknown and sumWall < thWall:
            return True
        else :
            return False


    def get_valid_cells(self, height, gridmap, width):

        #My extra code
        # Get Number of Explored Cells

        cells_explored = np.count_nonzero(gridmap > -1)

        rospy.loginfo("Cells Explored %i", cells_explored)

        # Create an Array with Cells to Pick
        cells = 0
        cells_close = 0
        cells_mid = 0
        cells_far = 0

        #cells_to_pick = np.zeros((cells_explored, 2))
        #cells_to_pick = np.zeros((cells_positive, 2))

        cells_to_pick_close = np.zeros((cells_explored, 2))
        cells_to_pick_mid = np.zeros((cells_explored, 2))
        cells_to_pick_far = np.zeros((cells_explored, 2))

        th_close = 80
        th_mid = 120

        for y in xrange(0, height):
            for x in xrange(0, width):
                idx = x + y * width
                if self.is_boundary(gridmap, idx, width):
                    #if gridmap[idx] > -1 and gridmap[idx] < mn:
                    #if gridmap[idx] > -1:
                    #if self.check_cell_region(gridmap, x, y, width):
                    if self.prevGoal is None or self.euclideanDistance_goal(self.prevGoal, x, y, th_close):
                        cells_to_pick_close[cells_close][0] = x
                        cells_to_pick_close[cells_close][1] = y
                        cells_close = cells_close + 1
                    elif self.prevGoal is None or self.euclideanDistance_goal(self.prevGoal, x, y, th_mid):
                        cells_to_pick_mid[cells_mid][0] = x
                        cells_to_pick_mid[cells_mid][1] = y
                        cells_mid = cells_mid + 1
                    else:
                        cells_to_pick_far[cells_far][0] = x
                        cells_to_pick_far[cells_far][1] = y
                        cells_far = cells_far + 1


        rospy.loginfo("***************************************")
        rospy.loginfo("***************************************")
        rospy.loginfo("***************************************")
        rospy.loginfo("Cells close %i", cells_close)
        rospy.loginfo("Cells mid %i", cells_mid)
        rospy.loginfo("Cells far %i", cells_far)

        if cells_mid > 20 and self.imStuck == False:
            cells_to_pick = np.resize(cells_to_pick_mid,(cells_mid,2))
        elif cells_far > 20:
            cells_to_pick = np.resize(cells_to_pick_far,(cells_far,2))
        else:
            cells_to_pick = np.resize(cells_to_pick_close,(cells_close,2))

        rospy.loginfo("***************************************")
        rospy.loginfo("***************************************")
        rospy.loginfo("***************************************")

        #cells_to_pick = np.resize(cells_to_pick,(cells,2))
        return cells_to_pick

    def is_boundary(self, gridmap, idx, width):
        if gridmap[idx] == 0 and (gridmap[idx-width-1] == -1 or gridmap[idx-width] == -1 or gridmap[idx-width+1] == -1 or gridmap[idx-1] == -1 or gridmap[idx+1] == -1 or gridmap[idx+width-1] == -1 or gridmap[idx+width] == -1 or gridmap[idx+width+1] == -1):
            bool = True
        else:
            bool = False

        return bool

    def euclideanDistance_goal(self, last, x, y, threshold):

        dist = np.sqrt(np.square(last[0] - x) + np.square(last[1] - y))

        if dist < threshold:
            return True
        else:
            return False



    # Send Goal as Simple Message (no feedback)
    def send_goal(self, goal):
        self.goal_pub.publish(goal)


if __name__ == '__main__':
    rospy.init_node('random_explorer',anonymous=True)
    explorer = RandomExplorer()
    explorer.loop()
