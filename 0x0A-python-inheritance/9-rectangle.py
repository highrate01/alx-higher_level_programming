#!/usr/bin/python3
"""Defines a class Rectangle than inherite from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return  self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        x = "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
        return x
