#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const nums = process.argv.slice(2);

if (nums.length < 2) {
  // Do nothing
}
const a = parseInt(nums[0]);
const b = parseInt(nums[1]);

const result = add(a, b);
console.log(result);
