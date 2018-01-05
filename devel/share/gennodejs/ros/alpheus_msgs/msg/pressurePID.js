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

class pressurePID {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pKp = null;
      this.pKi = null;
      this.pKd = null;
    }
    else {
      if (initObj.hasOwnProperty('pKp')) {
        this.pKp = initObj.pKp
      }
      else {
        this.pKp = 0.0;
      }
      if (initObj.hasOwnProperty('pKi')) {
        this.pKi = initObj.pKi
      }
      else {
        this.pKi = 0.0;
      }
      if (initObj.hasOwnProperty('pKd')) {
        this.pKd = initObj.pKd
      }
      else {
        this.pKd = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type pressurePID
    // Serialize message field [pKp]
    bufferOffset = _serializer.float32(obj.pKp, buffer, bufferOffset);
    // Serialize message field [pKi]
    bufferOffset = _serializer.float32(obj.pKi, buffer, bufferOffset);
    // Serialize message field [pKd]
    bufferOffset = _serializer.float32(obj.pKd, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type pressurePID
    let len;
    let data = new pressurePID(null);
    // Deserialize message field [pKp]
    data.pKp = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pKi]
    data.pKi = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pKd]
    data.pKd = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'alpheus_msgs/pressurePID';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b607b6b53844bf703ffc3df5d628e627';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 pKp
    float32 pKi
    float32 pKd
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new pressurePID(null);
    if (msg.pKp !== undefined) {
      resolved.pKp = msg.pKp;
    }
    else {
      resolved.pKp = 0.0
    }

    if (msg.pKi !== undefined) {
      resolved.pKi = msg.pKi;
    }
    else {
      resolved.pKi = 0.0
    }

    if (msg.pKd !== undefined) {
      resolved.pKd = msg.pKd;
    }
    else {
      resolved.pKd = 0.0
    }

    return resolved;
    }
};

module.exports = pressurePID;
