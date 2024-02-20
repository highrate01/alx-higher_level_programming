#!/usr/bin/python3
"""Defines a class and inherited class-checking  function"""


def is_kind_of_class(obj, a_class):
    """check if an obeject is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        if obj is an instance or inherited instance of a_class - True,
        otherwise - false.
    """
    return isinstance(obj, a_class):
