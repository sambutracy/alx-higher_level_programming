#!/usr/bin/node
// Filename: 101-sorted.js

const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (!sortedDict[occurrence]) {
    sortedDict[occurrence] = [];
  }
  sortedDict[occurrence].push(userId);
}

console.log(sortedDict);
