#!/usr/bin/node
// Filename: 6-square.js

'use strict';

const OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
