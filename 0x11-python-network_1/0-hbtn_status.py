#!/usr/bin/python3
"""
python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request(
            "https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        msg = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(msg)))
        print("\t- content: {}".format(msg))
        print("\t- utf88888888 content: {}".format(msg.decode(
            "utf-8")))
