#!/usr/bin/python3
"""Defines unittest for models/rectangle.py.

unittest classes:
    TestRectangle_instantiation
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_instantiation(unittest.TestCase):
    """Unittest for testing instantiation of Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 4), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_two_args(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(3, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(3, 5, 6)
        r2 = Rectangle(9, 10, 7)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(2, 0, 0, 8, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 4, 7, 8, 5)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle((3, 3, 0, 0, 1).__width))

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle((3, 3, 0, 0, 1).__height))

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle((3, 3, 0, 0, 1).__x))

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle((3, 3, 0, 0, 1).__y))

    def test_width_getter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        self.assertEqual(6, r.width)

    def test_width_setter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        self.assertEqual(7, r.x)

    def tesrt_x_setter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        self.assertEqual(9, r.y)

    def test_y_setter(self):
        r = Rectangle(6, 7, 7, 9, 1)
        r.y = 10
        self.assertEqual(10, r.y)
