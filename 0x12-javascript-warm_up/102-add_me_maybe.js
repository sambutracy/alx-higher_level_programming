#!/usr/bin/node
// Filename: 102-add_me_maybe.js

'use strict';

function addMeMaybe(number, theFunction) {
  theFunction(++number);
}

module.exports.addMeMaybe = addMeMaybe;
