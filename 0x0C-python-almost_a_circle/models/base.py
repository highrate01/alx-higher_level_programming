#!/usr/bin/python3
"""Defines a base model class"""
import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        It adds the class method that returns
        an instance with all attributes already set:
        """
        if dictionary and dictionary != []:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        It adds that class method
        that returns a list of instances:
        """
        n_file = "{}.json".format(cls.__name__)
        try:
            with open(n_file, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())

                _list = []
                for i in dict_list:
                    _list.append(cls.create(**i))
                return _list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Updats the class by serializes in CSV
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w") as csvfile:
            if list_objs is None or list_objs is []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        update class by deserilizes in csv
        """
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(csvfile, fieldnames=fieldnames)

                new_dict = []
                converted_dict = {}

                for row in dict_list:
                    for key, value in row.items():
                        converted_dict[key] = int(value)
                    new_dict.append(converted_dict)

                dict_list = new_dict
                instance_list = []
                for row in dict_list:
                    instance_list.append(cls.create(**row))

                return instance_list
        except FileNotFoundError:
            return []
