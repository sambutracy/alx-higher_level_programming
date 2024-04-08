#!/usr/bin/node
// Filename: 3-value_argument.js

'use strict';

const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
