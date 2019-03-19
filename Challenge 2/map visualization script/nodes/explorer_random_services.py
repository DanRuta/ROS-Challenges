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

from explorer_random import RandomExplorer

print("=================== explorer_random_services.py")

logFile = "/user/HS122/dr00392/chall2/src/turtlebot_explorer/nodes/outFile.txt"

class RandomExplorerServices(RandomExplorer):

    def __init__(self):

        print("new RandomExplorer explorer_random_services.py")

        with open(logFile, "a") as file:
            file.write("new RandomExplorer explorer_random_services.py\n")

        # Define a Service for Map
        rospy.wait_for_service('/dynamic_map')
        self.get_map_srv = rospy.ServiceProxy('/dynamic_map', GetMap)

        # Define a Simple Goal Publisher
        self.goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

    def update_map(self):

        try:
            map_resp = self.get_map_srv()
            assert isinstance(map_resp, GetMapResponse)

            if map_resp.map.info.width <= 64:  #Default size of map before any input (64x64)
                return False

            self.latest_map_msg = map_resp.map
            self.latest_map = np.array(self.latest_map_msg.data)
            print(self.latest_map_msg.info)

        except rospy.ServiceException, e:
            rospy.logwarn("Service call failed to get map: %s" % e)
            return False

        return True

    # Overwritten
    def loop(self):
        rate = rospy.Rate(0.1)

        while not rospy.is_shutdown():
            # rospy.loginfo("1 New Goal...")
            # rospy.loginfo("------------")

            if self.update_map():
                goal_msg = self.process_map()
                self.send_goal(goal_msg)

            rate.sleep()



if __name__ == '__main__':
    rospy.init_node('random_explorer_services')
    explorer = RandomExplorerServices()
    explorer.loop()
