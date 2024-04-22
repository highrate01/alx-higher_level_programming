#!/usr/bin/node

const args = process.argv.slice(2);
const number = args.map(arg => parseInt(arg));

if (number.length < 2) {
  console.log(0);
} else {
  const biggest = number.sort((a, b) => b - a);
  console.log(biggest[1]);
}
