#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    fetch = requests.get("https://alx-intranet.hbtn.io/status")

    print("Body responses:")
    print("\t- type: {}".format(type(fetch.text)))
    print("\t- content: {}".format(fetch.text))
