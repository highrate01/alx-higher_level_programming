#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new student.
        Args:
            first_name (str): The firstname of the student.
            last_name (str): Yhe last name of the student.
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary rep of the student if attribute
        is a list  of strings, represent only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent
        """
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if
                    hasattr(self, k)}
        return self.__dict__
