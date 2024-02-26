#!/usr/bin/python3
"""
Defines Square that inherits from Rectangle
"""
from models.rectangle import Rectangle



class Square(Rectangle):
    """
    The inherit class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        The getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """The setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Represents str
        """
        return "[square] ({}) {}/{} - {}".format(self.id,
                self.x,
                self.y,
                self.width)
