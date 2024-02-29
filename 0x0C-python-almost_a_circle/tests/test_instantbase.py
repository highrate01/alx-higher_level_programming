#!/usr/bin/python3
"""Defines instantiation bas"""
import unittest
import Base from models.base
from models.rectangle import Rectangle
from models.square import Square

class Test_instantiation_base(self):
    """Test for instatiation of the base"""

    def test_arg(self):
        """Test for no argument"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_bases(self):
        """Test for three bases"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None(self):
        """Test for no id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique(self):
        """Test for unique id"""
        self.assertEqual(12, Base(12).id)

    def test_instances_after_unique(self):
        """Test for nb instances in id"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_public_id(self):
        """test public id"""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def private_instanceid(self):
        """Test private id"""
        with self.assertRaises(AttrbuteError):
            print(base(12).__nb_instances)

    def test_str_id_(self):
        """Test for string in id"""
        self.assertEqual("hello", Base("hello").id)

    def teat_float_id(self):
        """test for float numbers"""
        self.assertEqual(3.3, Base(3.3).id)

    def test_complex_id(self):
        """test for complex numbers"""
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """test for dictionary list"""
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """test for boolean"""
        self.assertEqual(True, Base(True).id)

    def test_list(self):
        """test for list id"""
        self.assertEqual([1, 2, 3] Base([1, 2, 3]).id)

    def test_turple(self):
        """test for turple in id"""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """test for id set"""
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset(self):
        """test for frozen set"""
        self.assertEqual(frozenset({1, 2, 3}) Basefrozenset({1, 2, 3}).id)

    def test_range(self):
        """test for range id"""
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes(self):
        """test for bytes"""
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray(self):
        """test for the arrar of byte"""
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memory(self):
        """test for the memory"""
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_info(self):
        """test for the float inf"""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_float_Nan(self):
        """test if NAN in float is not equal"""
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_args(self):
        """test for two arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
