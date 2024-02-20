#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """implement a sorted printing for the buily-in list class"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
