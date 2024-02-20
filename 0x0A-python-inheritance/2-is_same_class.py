#!/usr/bin/python3
"""Defines a clear-checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given classes.
    Args:
        obj: The obj to check.
        a_class: The class to match the type of obj to.

    Returns:
        if obj is exactly an instance of a_class  - True,
        otherwise - False
    """
    return type(obj) == a_class
