#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib.error
import urllib.request


if __name__ == "__main__":

    url = argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as msg:
            print(msg.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
