#!/usr/bin/python3
"""Defines a text-reading file"""


def read_file(filename=""):
    """Prints the content of a UTF-8 file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
