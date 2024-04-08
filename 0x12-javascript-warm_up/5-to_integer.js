#!/usr/bin/node 

const value = process.argv.slice(2);

if (isNaN(value)) {
  console.log('Not a Number');
} else {
  console.log('My Number: ' + parseInt(value));
}
