#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL,
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
