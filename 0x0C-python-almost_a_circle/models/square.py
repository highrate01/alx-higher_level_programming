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
        return "[square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
            )

    def update(self, *args, **kwargs):
        """
        It adds the punlic method that assign attributes
        """
        if args:
            for i, attr in enumerate(args):
                if i == 0:
                    self.id = attr
                elif i == 1:
                    self.size = attr
                elif i == 2:
                    self.x = attr
                elif i == 3:
                    self.y = attr
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """
        It adds the public method that returns that
        returns the dictionary representation of a
        square
        """
        square_dict = {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
        return square_dict
