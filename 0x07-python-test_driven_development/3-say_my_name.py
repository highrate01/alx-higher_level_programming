#!/usr/bin/python3
"""Defines a name printing function"""


def say_my_name(first_name, last_name=None):
    """Print a name.
    
    Args:
        first_name (str): First name to print.
        last_name (str, optional): Last name to print.
        
    Raises:
        TypeError: if either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
        
    if last_name is not None and not isinstance(last_name, str):
        raise TypeError("last_name must be a string or None")
        
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
