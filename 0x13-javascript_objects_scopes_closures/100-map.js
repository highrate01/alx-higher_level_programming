#!/usr/bin/node

const arr = require('./100-data.js').arr;
console.log(arr);
console.log(arr.map((num, index) => num * index));
