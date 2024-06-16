#!/usr/bin/node

// Imports the Request Mdoule
const req = require('request');

// Checks number of arguments
if (process.argv.length < 3) {
  console.error('Error: Please provide the API URL as an argument.');
  process.exit(1);
}

// Assigns Movie ID and Url to Variable
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

// Coomputes all characters of a startwars Movie
req.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const i of dd) {
    req.get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
