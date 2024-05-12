#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""
from sys import argv
import requests


if __name__ == "__main_":
    url = "https://swapi.co/api/people"

    params = {"search": argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))
    [print(i.get("name")) for i in results.get("results")]
