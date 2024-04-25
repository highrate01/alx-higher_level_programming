#!/usr/bin/node

const fs = require('fs');
const fiA = fs.readFileSync(process.argv[2], 'utf8');
const fiB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fiA + fiB);
