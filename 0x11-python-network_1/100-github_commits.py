#!/usr/bin/python3
"""
lists 10 commits
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()

    count = 0

    for commit in commits:
        if count == 10:
            break
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")))
        count += 1
