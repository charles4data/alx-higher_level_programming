#!/usr/bin/node

// define function for searching for biggest int.
function findMax (...numbers) {
  if (numbers.length === 0 || numbers.length === 1) {
    return 0;
  }
  let maxNum = numbers[0];
  let i;

  for (i = 0; i < numbers.length; i++) {
    if (numbers[i] > maxNum) {
      maxNum = numbers[0];
    }
  }
  return maxNum;
}

const list = process.argv.slice(2).map(Number);

const max = findMax(...list);

console.log(max);
