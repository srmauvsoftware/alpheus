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

class offsetData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.offsetX = null;
      this.offsetY = null;
    }
    else {
      if (initObj.hasOwnProperty('offsetX')) {
        this.offsetX = initObj.offsetX
      }
      else {
        this.offsetX = 0.0;
      }
      if (initObj.hasOwnProperty('offsetY')) {
        this.offsetY = initObj.offsetY
      }
      else {
        this.offsetY = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type offsetData
    // Serialize message field [offsetX]
    bufferOffset = _serializer.float32(obj.offsetX, buffer, bufferOffset);
    // Serialize message field [offsetY]
    bufferOffset = _serializer.float32(obj.offsetY, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type offsetData
    let len;
    let data = new offsetData(null);
    // Deserialize message field [offsetX]
    data.offsetX = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [offsetY]
    data.offsetY = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'alpheus_msgs/offsetData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '796ae190d97828899df8883bfe807076';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 offsetX
    float32 offsetY
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new offsetData(null);
    if (msg.offsetX !== undefined) {
      resolved.offsetX = msg.offsetX;
    }
    else {
      resolved.offsetX = 0.0
    }

    if (msg.offsetY !== undefined) {
      resolved.offsetY = msg.offsetY;
    }
    else {
      resolved.offsetY = 0.0
    }

    return resolved;
    }
};

module.exports = offsetData;
