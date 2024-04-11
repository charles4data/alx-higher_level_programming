#!/usr/bin/node

exports.logMe = function (item) {
  // Use a static variable to keep track of the count
  if (typeof exports.logMe.count === 'undefined') {
    exports.logMe.count = 0;
  }

  console.log(exports.logMe.count + ': ' + item);
  exports.logMe.count++;
};
