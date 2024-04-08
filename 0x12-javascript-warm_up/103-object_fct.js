#!/usr/bin/node
// Filename: 103-object_fct.js

'use strict';

const myObject = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value++;
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
