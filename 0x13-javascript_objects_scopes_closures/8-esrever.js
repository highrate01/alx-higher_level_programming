#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight(function (array, curr) {
    array.push(curr);
    return array;
  }, []);
};
