#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) {
    console.error('Error writing to file:', error);
  } else {
    console.log(`Successfully wrote to file: ${filePath}`);
  }
});
