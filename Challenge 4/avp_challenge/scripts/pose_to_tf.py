#!/usr/bin/env python
import rospy

import math
import tf2_py
from tf import transformations as t
import tf2_ros
import geometry_msgs
import tf2_geometry_msgs

def pose_cb(pose_stamped):
    try:
        trans = tfBuffer.lookup_transform(source_frame, target_frame, rospy.Time(0))
    except (tf2_ros.LookupException):
        print("ERROR: LookupException!")
        return
    except (tf2_ros.ConnectivityException):
        print("ERROR: ConnectivityException!")
        return
    except (tf2_ros.ExtrapolationException):
        print("ERROR: ExtrapolationException!")
        return

    pose_transformed = tf2_geometry_msgs.do_transform_pose(pose_stamped, trans)
    pose_transformed.header.stamp = pose_stamped.header.stamp
    pose_transformed.header.seq = pose_stamped.header.seq

    rospy.loginfo_throttle(10,"Pose.   Frame_id:\t {}".format(pose_stamped.header.frame_id))
    rospy.loginfo_throttle(10,"Trans.  Frame_id:\t {}".format(trans.header.frame_id))
    rospy.loginfo_throttle(10,"PoseTF. Frame_id:\t {}".format(pose_transformed.header.frame_id))

    transform_stamped = geometry_msgs.msg.TransformStamped()
    transform_stamped.header.stamp = pose_transformed.header.stamp
    transform_stamped.header.seq = pose_transformed.header.seq
    transform_stamped.header.frame_id = pose_stamped.header.frame_id
    transform_stamped.child_frame_id = target_frame
    transform_stamped.transform.translation = pose_transformed.pose.position
    transform_stamped.transform.rotation = pose_transformed.pose.orientation
    broadcaster.sendTransform(transform_stamped)

if __name__ == '__main__':
    rospy.init_node('twizzy_pose_to_tf')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)
    broadcaster = tf2_ros.StaticTransformBroadcaster()

    source_frame = rospy.get_param('~source_frame', 'velodyne')
    target_frame = rospy.get_param('~target_frame', 'base_link')

    pose_sub = rospy.Subscriber("current_pose", geometry_msgs.msg.PoseStamped, pose_cb)

    rospy.spin()
