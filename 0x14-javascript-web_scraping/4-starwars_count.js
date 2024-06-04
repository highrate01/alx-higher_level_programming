#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const wedgeAntillesMovies = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(`${wedgeAntillesMovies.length}`);
  }
});
