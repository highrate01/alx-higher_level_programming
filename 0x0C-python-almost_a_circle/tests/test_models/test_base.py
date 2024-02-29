#!/usr/bin/python3
"""Defines unittest for base"""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class Test_create(unittest.TestCase):
    """unittest for create method"""

    def test_create_retangle(unittest.TestCase):
        Test1 = Rectangle(5, 3, 2, 1, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertEqual("[Rectanmgle] (7) 1/2 - 3/5", str(Test1))

    def 
