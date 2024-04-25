#!/usr/bin/node

const callMeMoby = (x, thefunction) => {
  if (x > 0) {
    thefunction();
    callMeMoby(x - 1, thefunction);
  }
};

module.exports.callMeMoby = callMeMoby;
