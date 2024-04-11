#!/usr/bin/node

// define function for searching for biggest int.
function findNum (...numbers) {
  if (numbers.length === 0 || numbers.length === 1) {
    return 0;
  }
  numbers.sort(function(a, b) {
    return b - a;
  });

  const second_biggest = numbers[1]; 

  return second_biggest;
}

const list = process.argv.slice(2).map(Number);

const max = findNum(...list);

console.log(max);
