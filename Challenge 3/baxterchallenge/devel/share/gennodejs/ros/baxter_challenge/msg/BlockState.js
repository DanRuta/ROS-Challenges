// Auto-generated. Do not edit!

// (in-package baxter_challenge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class BlockState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pose = null;
      this.block_colour = null;
      this.detected_colour = null;
    }
    else {
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new geometry_msgs.msg.Pose();
      }
      if (initObj.hasOwnProperty('block_colour')) {
        this.block_colour = initObj.block_colour
      }
      else {
        this.block_colour = '';
      }
      if (initObj.hasOwnProperty('detected_colour')) {
        this.detected_colour = initObj.detected_colour
      }
      else {
        this.detected_colour = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BlockState
    // Serialize message field [pose]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.pose, buffer, bufferOffset);
    // Serialize message field [block_colour]
    bufferOffset = _serializer.string(obj.block_colour, buffer, bufferOffset);
    // Serialize message field [detected_colour]
    bufferOffset = _serializer.string(obj.detected_colour, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BlockState
    let len;
    let data = new BlockState(null);
    // Deserialize message field [pose]
    data.pose = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    // Deserialize message field [block_colour]
    data.block_colour = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [detected_colour]
    data.detected_colour = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.block_colour.length;
    length += object.detected_colour.length;
    return length + 64;
  }

  static datatype() {
    // Returns string type for a message object
    return 'baxter_challenge/BlockState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '64375395e16156e7524bad1bd00751b2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    geometry_msgs/Pose pose
    string block_colour
    string detected_colour
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BlockState(null);
    if (msg.pose !== undefined) {
      resolved.pose = geometry_msgs.msg.Pose.Resolve(msg.pose)
    }
    else {
      resolved.pose = new geometry_msgs.msg.Pose()
    }

    if (msg.block_colour !== undefined) {
      resolved.block_colour = msg.block_colour;
    }
    else {
      resolved.block_colour = ''
    }

    if (msg.detected_colour !== undefined) {
      resolved.detected_colour = msg.detected_colour;
    }
    else {
      resolved.detected_colour = ''
    }

    return resolved;
    }
};

module.exports = BlockState;
