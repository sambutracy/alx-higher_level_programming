#!/usr/bin/node
// Filename: 5-square.js

'use strict';

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
