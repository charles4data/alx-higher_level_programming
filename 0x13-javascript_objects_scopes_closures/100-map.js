#!/usr/bin/node

// importing list
const list = require('./100-data.js').list;

// Using map on the list
const newList = list.map((x, i) => x * i);

// print lists
console.log(list);
console.log(newList);
