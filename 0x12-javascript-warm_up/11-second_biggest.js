#!/usr/bin/node
// Filename: 11-second_biggest.js

'use strict';

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
