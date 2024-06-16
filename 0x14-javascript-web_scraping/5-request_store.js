#!/usr/bin/node

// Imports the rquest and file system Modules
const request = require('request');
const fs = require('fs');

// Gets ad stores the contents of a webpage and stores it in a file.
request(process.argv[2], function (err, response, body) {
  if (err == null) {
    fs.writeFileSync(process.argv[3], body);
  }
});
