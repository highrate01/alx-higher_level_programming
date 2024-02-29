#!/usr/bin/python3
"""
Defines unittest for base
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square

class Test_base_create(unittest.TestCase):
    """Testing for the Base Class"""

    def test_rectangle_create(self):
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertEqua("[Rectangle] (7) 1/2 - 3/5", str(Test1))

    def test_craete_new_rectangle(self):
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(Test2))

    def test_create_equal_rectangle(self):
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertIsNot(Test1, Test2)

    def test_equal_rectangle_create(self):
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertNotEqual(Test1, Test2)

    def test_creat_square(self):
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_new_square(self):
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_is_square(self):
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_create_equal_square(self):
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)

if __name == "__main__":
    unittest.main()
