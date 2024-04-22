#!/usr/bin/node 

const num_args = process.argv.length;

if (num_args === 2)
{
	console.log('No argument');
}
else if (num_args === 3)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}
