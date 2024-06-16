#!/usr/bin/node

// Imports the Request Mdoule
const request = require('request');

// Checks number of arguments
if (process.argv.length < 3) {
  console.error('Error: Please provide the API URL as an argument.');
  process.exit(1);
}

// Computes the url using api and movie id
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

// Prints all characters of a Star Wars movie
function printCharacters (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
