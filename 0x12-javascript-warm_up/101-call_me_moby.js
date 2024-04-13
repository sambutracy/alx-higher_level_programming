#!/usr/bin/node
// Filename: 101-call_me_moby.js

'use strict';

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
