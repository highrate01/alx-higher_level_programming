#!/bin/bash

# Send HEAD request to URL and get Content-Length header
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
