// Auto-generated. Do not edit!

// (in-package baxter_challenge.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ObjectInspectionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ObjectInspectionRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ObjectInspectionRequest
    let len;
    let data = new ObjectInspectionRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'baxter_challenge/ObjectInspectionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ObjectInspectionRequest(null);
    return resolved;
    }
};

class ObjectInspectionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.colour = null;
    }
    else {
      if (initObj.hasOwnProperty('colour')) {
        this.colour = initObj.colour
      }
      else {
        this.colour = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ObjectInspectionResponse
    // Serialize message field [colour]
    bufferOffset = _serializer.string(obj.colour, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ObjectInspectionResponse
    let len;
    let data = new ObjectInspectionResponse(null);
    // Deserialize message field [colour]
    data.colour = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.colour.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'baxter_challenge/ObjectInspectionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b7b93667ab19d45333d9d3fab6d6a1fb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string colour
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ObjectInspectionResponse(null);
    if (msg.colour !== undefined) {
      resolved.colour = msg.colour;
    }
    else {
      resolved.colour = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: ObjectInspectionRequest,
  Response: ObjectInspectionResponse,
  md5sum() { return 'b7b93667ab19d45333d9d3fab6d6a1fb'; },
  datatype() { return 'baxter_challenge/ObjectInspection'; }
};
