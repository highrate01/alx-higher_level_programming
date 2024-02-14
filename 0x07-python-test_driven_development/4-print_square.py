#!/usr/bin/python3
"""Defines a square printing function"""


def print_square(size):
    """This function prints square with
    # character.
    Args:
        size: The height/width of the square.
    Raises:
        TypeError: if size is an integer
        ValueError: if size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
