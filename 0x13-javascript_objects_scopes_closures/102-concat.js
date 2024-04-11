#!/usr/bin/node

// import file system
const fs = require('fs');

// read files
const a = fs.readFileSync(process.argv[2], 'utf8');
const b = fs.readFileSync(process.argv[3], 'utf8');

// concat files
fs.writeFileSync(process.argv[4], a + '\n' + b);
