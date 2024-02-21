#!/usr/bin/python3
"""Defines JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to text file usin JSON
    representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
