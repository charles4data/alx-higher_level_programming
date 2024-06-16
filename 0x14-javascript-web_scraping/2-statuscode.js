#!/usr/bin/node

// import request
const request = require('request');

// Assign URL to variable
const URL = process.argv[2];

// Get and display the status code
request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
