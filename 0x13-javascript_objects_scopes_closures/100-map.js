#!/usr/bin/node

// importing list
const list = require('./100-data').list;

// Using map on the list
const newList = list.map((x, index) => x * index);

// print lists
console.log(list);
console.log(newList);
