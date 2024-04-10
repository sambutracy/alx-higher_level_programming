#!/usr/bin/node
// Filename: 102-concat.js

const fs = require('fs');

const [, , fileA, fileB, fileC] = process.argv;

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }

    const concatenatedData = `${dataA}${dataB}`;

    fs.writeFile(fileC, concatenatedData, err => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Files ${fileA} and ${fileB} have been concatenated into ${fileC}`);
    });
  });
});
