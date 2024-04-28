#!/usr/bin/node

// Declare and initialize args
const args = process.argv.slice(2);

// Conditional printing
if (args.length === 0) {
  const args1 = 'undefined';
  const args2 = 'undefined';
  console.log(args1 + ' is ' + args2);
} else if (args.length === 1) {
  const args1 = args[0];
  const args2 = 'undefined';
  console.log(args1 + ' is ' + args2);
} else {
  const args1 = args[0];
  const args2 = args[1];
  console.log(args1 + ' is ' + args2);
}
