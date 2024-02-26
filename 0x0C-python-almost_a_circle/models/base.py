#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """Represents the base model"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        It adding the static method that returns
        the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        to_json = json.dumps(list_dictionaries)
        return to_json
