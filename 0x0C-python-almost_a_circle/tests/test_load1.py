#!/usr/bin/python3
"""Defines unittest base"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square

class TestBase(unittest.TestCase):
    """unittest for testing load file method
    from csv
    """
    @classmethod
    def dlit_file(self):
        """tests for deleted created file"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

   def  test_loadfrom_firstrectangle(self):
       """Test loaded file from first rectangle"""
       r1 = Rectangle(10, 7, 8, 9)
       r2 = Rectangle(2, 4, 5, 6, 2)
       Rectangle.save_to_file([r1, r2])
       output_rectangle = Rectangle.load_from_file()
       self.assertEqual(str(r1), str(output_rectangle[0]))

    def test_loadfrom_secondrect(self):
        """Test loaded from second rectangle"""
        r1 = rectangle(10, 7, 8, 9)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(output[1]))

    def load_file_rect_type(self):
        """test for rectangle type"""
        r1 = Rectangle(10, 7, 8, 9)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def  test_loadfrom_firstrsquare(self):
       """Test loaded file from first Square"""
       s1 = Square(10, 7, 8, 9)
       s2 = Square(4, 5, 6, 2)
       Square.save_to_file([r1, r2])
       output_square = Square.load_from_file()
       self.assertEqual(str(r1), str(output_square[0]))

    def test_loadfrom_secondsquare(self):
        """Test loaded from second square"""
        s1 = rectangle(10, 7, 8, 9)
        s2 = Square(4, 5, 6, 2)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(r2), str(output[1]))
        
    def load_file_square_type(self):
        """test for square type"""
        s1 = Square(10, 7, 8, 9)
        s2 = Square(4, 5, 6, 2)
        Square.save_to_file([r1, r2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_no_file(self):
        """test for no file"""
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_more than one_args(self):
        """test for more than one arguments"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

if __name__ == "__main__":
    unittest.main()
