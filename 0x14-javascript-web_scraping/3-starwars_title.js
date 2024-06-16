#!/usr/bin/node

// Import the request module
const request = require('request');

// Get episode number
const movieid = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

// Prints the title of starwars movie
request(API_URL + movieid, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
