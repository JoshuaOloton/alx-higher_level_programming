#!/usr/bin/node
if (parseInt(process.argv[2]) === NaN || process.argv[2] === undefined ) {
    console.log('Not a number');
} else {
    console.log(`Number: ${process.argv[2]}`)
}
