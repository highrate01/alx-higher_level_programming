#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    const antilles = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
    console.log(`${antilles.length}`);
  }
});
