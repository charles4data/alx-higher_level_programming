#!/usr/bin/node

// computing the factorial
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }

  // ensure its a number
  num = parseInt(num);

  // base case
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

// getting first argument
const num = process.argv.slice(2);

// computing the factorial of a given number
const result = factorial(num);

// printing the result
console.log(result);
