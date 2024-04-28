#!/usr/bin/node

// defining the rectangle class
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0 && Number.isInteger(w)) && (h > 0 && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is invalid
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
