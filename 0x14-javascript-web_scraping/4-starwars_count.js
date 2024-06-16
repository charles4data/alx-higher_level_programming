#!/usr/bin/node

// Importing the Request Module
const request = require('request');

// Assign URL to variable
const API_URL = process.argv[2];

// prints the number of movies where the character
// “Wedge Antilles” is present.
request(API_URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movieIndex in movies) {
      const movieCharachers = movies[movieIndex].characters;
      for (const characterIndex in movieCharacters) {
        if (movieCharacters[characterIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});