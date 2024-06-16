#!/usr/bin/node

// Import the Request Module
const request = require('request');

// Checks number of arguments
if (process.argv.length < 3) {
  console.error('Error: Please provide the API URL as an argument.');
  process.exit(1);
}

// Assign URL to Variable
const url = process.argv[2];

// Computes the number of tasks completed by user id
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
