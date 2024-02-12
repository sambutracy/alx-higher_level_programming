#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import unittest
import io
import unittest.mock
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)

    def test_init_with_args(self):
        rectangle = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 5)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle("invalid", 4)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(-3, 4)

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3, "invalid")
        with self.assertRaises(ValueError):
            rectangle = Rectangle(3, -4)

    def test_x_validation(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3, 4, "invalid", 2)
        with self.assertRaises(ValueError):
            rectangle = Rectangle(3, 4, -1, 2)

    def test_y_validation(self):
        with self.assertRaises(TypeError):
            rectangle = Rectangle(3, 4, 1, "invalid")
        with self.assertRaises(ValueError):
            rectangle = Rectangle(3, 4, 1, -2)

    def test_area(self):
        rectangle = Rectangle(3, 4)
        self.assertEqual(rectangle.area(), 12)

    def test_display(self):
        rectangle = Rectangle(3, 2)
        expected_output = "   ###\n   ###\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_to_dictionary(self):
        rectangle = Rectangle(3, 4, 1, 2, 5)
        expected_dict = {'id': 5, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)
