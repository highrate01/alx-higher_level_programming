#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == "__main_":
    username = argv[1]
    password = argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data["id"])
    else:
        print("None")
