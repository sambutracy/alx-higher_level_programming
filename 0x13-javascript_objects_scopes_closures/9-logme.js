#!/usr/bin/node
// Filename: 9-logme.js

'use strict';

let count = 0;

exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
