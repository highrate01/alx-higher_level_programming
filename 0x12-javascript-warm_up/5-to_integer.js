#!/usr/bin/node

const arg2 = process.argv[2];
const conNum = parseInt(arg2);

if (isNaN(conNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${conNum}`);
}
