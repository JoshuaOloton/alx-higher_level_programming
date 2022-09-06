#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log(`Number: ${process.argv[2]}`);
}
