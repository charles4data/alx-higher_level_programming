#!/usr/bin/node

const x = process.argv.slice(2);

const size = parseInt(x);
let i;
let j;

if (isNaN(size)) {
  console.log('Missing Size');
}

if (size <= 0) {
	// do nothing
}

for (i = 0; i < size; i++) {
  let row = '';
  for (j = 0; j < size; j++) {
    row +='x';
  }
  console.log(row);
}
