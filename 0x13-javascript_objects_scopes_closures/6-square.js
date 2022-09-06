#!/usr/bin/node
const OldSqaure = require('./5-square');
module.exports = class Square extends OldSqaure {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write('C');
        }
      }
      process.stdout.write('\n');
    }
  }
};
