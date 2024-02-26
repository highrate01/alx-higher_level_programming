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
        It adds the static method that returns
        the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        to_json = json.dumps(list_dictionaries)
        return to_json

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It adds the class method that writes the JSON string
        representation of list_objs to a file
        """
        n_file = "{}.json".format(cls.__name__)
        with open(n_file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("{}")
            else:
                dict_list = []
                for obj in list_objs:
                    dict_list.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(dict_list))

    def from_json_string(json_string):
        """
        It adds the static method that
        returns the list of the JSON string representation
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
