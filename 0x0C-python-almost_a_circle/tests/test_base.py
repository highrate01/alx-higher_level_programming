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
        """
        test for creating a rectangle and comparing
        its string
        """
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertEqua("[Rectangle] (7) 1/2 - 3/5", str(Test1))

    def test_craete_new_rectangle(self):
        """
        test creating a new rectangle and comparing its string
        representation
        """
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(Test2))

    def test_create_equal_rectangle(self):
        """
        test that the created rectangle is not the same
        object as the original
        """
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertIsNot(Test1, Test2)

    def test_equal_rectangle_create(self):
        """test for not equal rectangle"""
        Test1 = Rectangle(3, 1, 5, 2, 7)
        Test1_dictionary = Test1.to_dictionary()
        Test2 = Rectangle.create(**Test1_dictionary)
        self.assertNotEqual(Test1, Test2)

    def test_creat_square(self):
        """
        test for creation of a
        square module
        """
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_new_square(self):
        """
        test for craetion of a new square module
        """
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_is_square(self):
        """
        Test for the created square is not the same as
        the original
        """
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertIsNot(sq1, sq2)

    def test_create_equal_square(self):
        """Test for not equal square"""
        sq1 = Square(5, 1, 3, 7)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)
        self.assertNotEqual(sq1, sq2)

if __name == "__main__":
    unittest.main()
