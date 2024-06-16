#!/usr/bin/node

// Import the Node.js file system module
const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
  console.error('Error: Please provide the file path as an argument.');
  process.exit(1);
}

const filePath = process.argv[2];

// Read the file using utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
  } else {
    console.log(data);
  }
});
