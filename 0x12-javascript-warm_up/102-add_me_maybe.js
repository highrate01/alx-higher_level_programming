#!/usr/bin/node

const addMeMaybe = (number, thefunction) => {
  number++;
  thefunction(number);
};

module.exports.addMeMaybe = addMeMaybe;
