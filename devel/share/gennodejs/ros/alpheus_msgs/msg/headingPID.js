// Auto-generated. Do not edit!

// (in-package alpheus_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class headingPID {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.hKp = null;
      this.hKi = null;
      this.hKd = null;
    }
    else {
      if (initObj.hasOwnProperty('hKp')) {
        this.hKp = initObj.hKp
      }
      else {
        this.hKp = 0.0;
      }
      if (initObj.hasOwnProperty('hKi')) {
        this.hKi = initObj.hKi
      }
      else {
        this.hKi = 0.0;
      }
      if (initObj.hasOwnProperty('hKd')) {
        this.hKd = initObj.hKd
      }
      else {
        this.hKd = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type headingPID
    // Serialize message field [hKp]
    bufferOffset = _serializer.float32(obj.hKp, buffer, bufferOffset);
    // Serialize message field [hKi]
    bufferOffset = _serializer.float32(obj.hKi, buffer, bufferOffset);
    // Serialize message field [hKd]
    bufferOffset = _serializer.float32(obj.hKd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type headingPID
    let len;
    let data = new headingPID(null);
    // Deserialize message field [hKp]
    data.hKp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [hKi]
    data.hKi = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [hKd]
    data.hKd = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'alpheus_msgs/headingPID';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '19a0fa31de3cf3c925595e656db1566d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 hKp
    float32 hKi
    float32 hKd
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new headingPID(null);
    if (msg.hKp !== undefined) {
      resolved.hKp = msg.hKp;
    }
    else {
      resolved.hKp = 0.0
    }

    if (msg.hKi !== undefined) {
      resolved.hKi = msg.hKi;
    }
    else {
      resolved.hKi = 0.0
    }

    if (msg.hKd !== undefined) {
      resolved.hKd = msg.hKd;
    }
    else {
      resolved.hKd = 0.0
    }

    return resolved;
    }
};

module.exports = headingPID;
