#!/usr/bin/node

// 1. Import the dictionary
const dict = require('./101-data').dict;

// 2. Reverse the dictionary
const occurrencesByUser = {};

for (const userId in dict) {
  const count = dict[userId];
  if (!occurrencesByUser[count]) {
    occurrencesByUser[count] = [];
  }
  occurrencesByUser[count].push(userId);
}

// 3. Print the inverted dictionary
console.log(occurrencesByUser);
