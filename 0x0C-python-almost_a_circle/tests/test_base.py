#!/usr/bin/python3
"""defines unittest for base.py.

Unnittest classes:
    Testbase_instantiation
"""


import unittest
import os
from models.base import Base

class Testbase_instantion(unittest.TestCase):
    """Unittest for the instantiation of class base."""
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 10
        self.assertEqual(10, b.id)

    def test_nb_instasnces_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_float_id(self):
        self.assertEqual(8.2, Base(8.2).id)

    def test_str_id(self):
        self.assertEqual("Hello", Base("Hello").id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2, "hello"), Base((1, 2, "hello")).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_range_id(self):
        self.assertEqual(range(9), Base(range(9)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base((b'Python')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 3)

if __name__ == "__main__":
    unittest.main()
