#!/usr/bin/node

const value = process.argv.slice(2);

const num = parseInt(value);

if (isNaN(num)) {
  console.log('Not a Number');
} else {
  console.log('My Number: ' + num);
}
