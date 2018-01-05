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

class thruster {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.speedfwd1 = null;
      this.speedfwd2 = null;
      this.speedup1 = null;
      this.speedup2 = null;
      this.speedup3 = null;
      this.speedup4 = null;
      this.speeddir1 = null;
      this.speeddir2 = null;
    }
    else {
      if (initObj.hasOwnProperty('speedfwd1')) {
        this.speedfwd1 = initObj.speedfwd1
      }
      else {
        this.speedfwd1 = 0;
      }
      if (initObj.hasOwnProperty('speedfwd2')) {
        this.speedfwd2 = initObj.speedfwd2
      }
      else {
        this.speedfwd2 = 0;
      }
      if (initObj.hasOwnProperty('speedup1')) {
        this.speedup1 = initObj.speedup1
      }
      else {
        this.speedup1 = 0;
      }
      if (initObj.hasOwnProperty('speedup2')) {
        this.speedup2 = initObj.speedup2
      }
      else {
        this.speedup2 = 0;
      }
      if (initObj.hasOwnProperty('speedup3')) {
        this.speedup3 = initObj.speedup3
      }
      else {
        this.speedup3 = 0;
      }
      if (initObj.hasOwnProperty('speedup4')) {
        this.speedup4 = initObj.speedup4
      }
      else {
        this.speedup4 = 0;
      }
      if (initObj.hasOwnProperty('speeddir1')) {
        this.speeddir1 = initObj.speeddir1
      }
      else {
        this.speeddir1 = 0;
      }
      if (initObj.hasOwnProperty('speeddir2')) {
        this.speeddir2 = initObj.speeddir2
      }
      else {
        this.speeddir2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type thruster
    // Serialize message field [speedfwd1]
    bufferOffset = _serializer.uint16(obj.speedfwd1, buffer, bufferOffset);
    // Serialize message field [speedfwd2]
    bufferOffset = _serializer.uint16(obj.speedfwd2, buffer, bufferOffset);
    // Serialize message field [speedup1]
    bufferOffset = _serializer.uint16(obj.speedup1, buffer, bufferOffset);
    // Serialize message field [speedup2]
    bufferOffset = _serializer.uint16(obj.speedup2, buffer, bufferOffset);
    // Serialize message field [speedup3]
    bufferOffset = _serializer.uint16(obj.speedup3, buffer, bufferOffset);
    // Serialize message field [speedup4]
    bufferOffset = _serializer.uint16(obj.speedup4, buffer, bufferOffset);
    // Serialize message field [speeddir1]
    bufferOffset = _serializer.uint16(obj.speeddir1, buffer, bufferOffset);
    // Serialize message field [speeddir2]
    bufferOffset = _serializer.uint16(obj.speeddir2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type thruster
    let len;
    let data = new thruster(null);
    // Deserialize message field [speedfwd1]
    data.speedfwd1 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speedfwd2]
    data.speedfwd2 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speedup1]
    data.speedup1 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speedup2]
    data.speedup2 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speedup3]
    data.speedup3 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speedup4]
    data.speedup4 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speeddir1]
    data.speeddir1 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [speeddir2]
    data.speeddir2 = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'alpheus_msgs/thruster';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '016d61562410ee3b17201a66aa29be18';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 speedfwd1
    uint16 speedfwd2
    uint16 speedup1
    uint16 speedup2
    uint16 speedup3
    uint16 speedup4
    uint16 speeddir1
    uint16 speeddir2
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new thruster(null);
    if (msg.speedfwd1 !== undefined) {
      resolved.speedfwd1 = msg.speedfwd1;
    }
    else {
      resolved.speedfwd1 = 0
    }

    if (msg.speedfwd2 !== undefined) {
      resolved.speedfwd2 = msg.speedfwd2;
    }
    else {
      resolved.speedfwd2 = 0
    }

    if (msg.speedup1 !== undefined) {
      resolved.speedup1 = msg.speedup1;
    }
    else {
      resolved.speedup1 = 0
    }

    if (msg.speedup2 !== undefined) {
      resolved.speedup2 = msg.speedup2;
    }
    else {
      resolved.speedup2 = 0
    }

    if (msg.speedup3 !== undefined) {
      resolved.speedup3 = msg.speedup3;
    }
    else {
      resolved.speedup3 = 0
    }

    if (msg.speedup4 !== undefined) {
      resolved.speedup4 = msg.speedup4;
    }
    else {
      resolved.speedup4 = 0
    }

    if (msg.speeddir1 !== undefined) {
      resolved.speeddir1 = msg.speeddir1;
    }
    else {
      resolved.speeddir1 = 0
    }

    if (msg.speeddir2 !== undefined) {
      resolved.speeddir2 = msg.speeddir2;
    }
    else {
      resolved.speeddir2 = 0
    }

    return resolved;
    }
};

module.exports = thruster;
