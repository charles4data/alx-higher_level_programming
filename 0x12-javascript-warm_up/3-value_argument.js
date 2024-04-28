#!/usr/bin/node

// Get all command line arguments
const args = process.argv.slice(2);

// Check and print argument
if (args[0]) {
  console.log(args[0]);
} else {
  console.log('No argument');
}
