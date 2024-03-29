#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class for base model
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        it returns the area value of the Rectangle instanc
        """
        area = self.width * self.height
        return area

    def display(self):
        """Display"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[rectangle] ({})  {}/{} - {}/{}".format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width,
                                                        self.height)

    def update(self, *args, **kwargs):
        """
        Assigns keys or values to attributes
        base on thier position
        """
        if args:
            for i, attr in enumerate(args):
                if i == 0:
                    self.id = attr
                elif i == 1:
                    self.width = attr
                elif i == 2:
                    self.height = attr
                elif i == 3:
                    self.x = attr
                elif i == 4:
                    self.y = attr
                else:
                    continue
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """
        It adds the pubic method that returns the dictionary
        representation of Rectangle
        """
        dict_rec = {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
        return dict_rec
