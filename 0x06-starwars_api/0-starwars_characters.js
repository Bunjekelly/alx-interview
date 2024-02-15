#!/usr/bin/node

//a script that prints all characters of a Star Wars movie


const https = require('https');

const get = (url) => {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        resolve(JSON.parse(data));
      });
    }).on('error', (err) => {
      reject(err.message);
    });
  });
};

const printCharacters = async (movieId) => {
  try {
    const response = await get(`https://swapi.dev/api/films/${movieId}/`);
    const characterUrls = response.characters;

    for (const url of characterUrls) {
      const character = await get(url);
      console.log(character.name);
    }
  } catch (error) {
    console.error(`Failed to get movie with ID ${movieId}: ${error}`);
  }
};

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: node script.js <movie_id>');
} else {
  printCharacters(movieId);
}
