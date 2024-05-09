#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL,
# and displays the body of the response

if [ -z "$1" ]; then
	echo "Usage: $0 <url>"
	exit 1
fi

response=$(curl -s "$1")

body_size=${#response}

echo "$body_size"

