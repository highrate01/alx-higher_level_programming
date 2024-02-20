#!/usr/bin/python3
"""Defines a base geometry of class BaseGeometry."""


class BaseGeometry:
    """Represent Base Geometry"""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a perimeter as an integer.
        Args:
            name (str): The name of the perimeter
            value (int): The perimeter to validate.
        Returns:
            TypeError: if the type is not an integer
            ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
