#!/usr/bin/node

// importing list
const list1 = require('./100-data').list;

// Using map on the list
const newList = list1.map((x, index) => x * index);

// print lists
console.log(list1);
console.log(newList);
