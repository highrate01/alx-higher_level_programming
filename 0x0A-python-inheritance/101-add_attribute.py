#!/usr/bin/python3
"""Defines a function that adds attributes to object."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Args:
        obj (any): The object to an attribute to
        att (str): The name of the attribute to add
        value (any): The value of the attribute
    Returns:
        TypeError: if the attriute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
