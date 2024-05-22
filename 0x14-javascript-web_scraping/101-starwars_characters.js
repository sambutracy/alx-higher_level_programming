#!/usr/bin/node
const request = require('request');

// Extract the movie ID from command-line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to fetch film data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const film = JSON.parse(body);

  // Retrieve the list of characters from the film data
  const characters = film.characters;

  // Iterate over each character URL and make a request to fetch character data
  characters.forEach(characterUrl => {
    request(characterUrl, (err, res, characterBody) => {
      if (err) {
        console.error(err);
        return;
      }

      // Parse the character data
      const characterData = JSON.parse(characterBody);

      // Print the name of the character
      console.log(characterData.name);
    });
  });
});
