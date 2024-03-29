#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width(int): The width of the new rectangle
            height(int): The height of the new Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the new Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the Rectangle"""
        return self.__height

    @height.setter
    def height
