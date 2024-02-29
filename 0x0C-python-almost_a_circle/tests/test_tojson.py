#!/usr/bin/python3

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Test_baseto_jsonstring(unittest.Testcase):
    """Unittest for testing to_json_strin
    method of base class"""

    def to_json_rectangle(self):
        """test for rectangle type module"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_onedict_rect(self):
        """test for dict in rectagle"""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_two_dict_rect(self):
        """Test for more than one dict in rect"""
        r = Rectangle(10, 7, 2, 8, 6)
        r1 = Rectangle(9, 8, 4, 5, 6)
        dict_list = [r.to_dictionary(), r1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 109)

    def test_square_type(self):
        """test for square type"""
        s = Square(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_square_one_dict(self):
        """test for dict in square"""
        s = Square(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()]))== 40)

    def test_square_two_dict(self):
        """test for two dicts in square"""
        s = Square(10, 7, 2, 8, 6)
        s1 = Square(9, 8, 4, 5, 6)
        dict_list = [s.to_dictionary(), s1.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dict_list)) == 80)

    def test_empty_list(self):
        """test for empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """test for none"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        """test for no argument"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arguments(self):
        """test for more arguments"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)
