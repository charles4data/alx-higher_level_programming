#!/usr/bin/node

// Import Node.js file system module
const fs = require('fs');

// Check for arguments
if (process.argv.length < 4) {
  console.error("Error: Please provide both file path and string to write as arguments.");
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write to file using UTF-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error("Error writing to file:", err); // Print error object on failure
  } else {
    console.log(`Successfully wrote "${stringToWrite}" to ${filePath}`);
  }
});
