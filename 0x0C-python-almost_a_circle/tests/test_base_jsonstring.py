#!/usr/bin/python3
"""unittest for base"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import os

class TestBase_jsonstring(unittest.TestCase):
    """Tests for json_string method of Base class"""

    def test_jsonstring_type(self):
        """Test for output list"""
        input_list = [{"id": 70, "width": 20, "height": 5}]
        input_list_json = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(input_list_json)
        self.assertEqual(list, type(output_list))

    def test_jsonstring_one_rectangle(self):
        """test for deserialized output correctness"""
        input_list = [{"id": 70, "width": 20, "height": 5}]
        input_list_json = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(input_list_json)
        self.assertEqual(input_list, output_list)

    def test_jsonstring_two_rectangle(self):
        """Test for deserialized output for two rectangles"""
        
        input_list = [
                {"id": 70, "width": 12, "height": 5, "x": 9, "y": 8},
                {"id": 79, "width": 7, "height": 4, "x": 8, "y": 7},
            ]
        input_list_json = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(input_list_json)
        self.assertEqual(input_list, output_list)

    def test_jsonstring_one_square(self):
        """Test for desrialized output for a single square"""
        input_list = [{"id": 70, "size": 8, "height": 6}]
        input_list_json = Square.to_json_string(input_list)
        output_list = Square.from_json_string(input_list_json)
        self.assertEqual(input_list, output_list)

    def test_jsonstring_two_square(self):
        """Test for deserialized output for two squares"""
        input_list = [
                {"id": 70, "size": 20, "height": 8},
                {"id": 9, "size": 2, "height": 8},
        ]
        input_list_json = Square.to_json_string(input_list)
        output_list = Square.from_json_string(input_list_json)
        self.assertEqual(input_list, output_list)

    def test_from_json_none_string(self):
        """Test for deserialized empty list"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_json_no_args(self):
        """Test for no arguments provided"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_json_more_than_one_args(self):
        """Test for more than one arguments provided"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

if __name__ == "__main__":
    unittest.main()
