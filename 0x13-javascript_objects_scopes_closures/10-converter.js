#!/usr/bin/node
// Filename: 10-converter.js

'use strict';

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
