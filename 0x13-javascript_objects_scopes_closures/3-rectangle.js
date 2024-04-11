#!/usr/bin/node

// Define a Rectangle class
module.exports = class Rectangle {
  costructor (w, h) {
    if (w <= 0 || h <= 0) {
      // Do nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
