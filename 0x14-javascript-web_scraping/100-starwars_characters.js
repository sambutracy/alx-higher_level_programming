#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
