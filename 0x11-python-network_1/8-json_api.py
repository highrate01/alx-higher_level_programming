#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]

    payload = {"q": letter}

    fetch = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        msg = fetch.json()
        if msg == {}:
            print("No result")
        else:
            print("[{}] {}".format(msg.get("id"), msg.get("name")))
    except ValueError:
        print("Not a valid JSON")
