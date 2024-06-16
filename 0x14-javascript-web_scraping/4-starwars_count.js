#!/usr/bin/node

// Import the request module
const request = require('request');

if (process.argv.length < 3) {
  console.error('Error: Please provide the Star Wars API URL as an argument.');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];
const characterId = 18;

// Fetch film data from the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  // Parse the JSON response
  try {
    const films = JSON.parse(body).results;

    // Filter for films with Wedge Antilles
    const filmsWithWedge = films.filter(film => {
      return film.characters.includes(apiUrl + 'people/' + characterId);
    });

    // Print the count
    console.log(filmsWithWedge.length);
  } catch (jsonError) {
    console.error('Error parsing JSON:', jsonError);
  }
});
