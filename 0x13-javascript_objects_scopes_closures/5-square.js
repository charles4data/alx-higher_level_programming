#!/usr/bin/node

// Import Rectangle class
const Rectangle = require('./4-rectangle');

// Creates square class
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
