#!/usr/bin/node

const data = require('./101-data.js').data;
let newDict = {}

for (let key in data) {
	if (newDict[data[key]] === undefined) {
		newDict[data[key]] = [key];
	} else {
		newDict[data[key]].push(key);
	}
}
console.log(newDict);
