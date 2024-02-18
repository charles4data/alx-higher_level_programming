#!/usr/bin/python3

import unittest
from models import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        rect = Rectangle(5, 3, 2, 4, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def test_init(self):
        rect1 = Rectangle(5, 3, 2, 4, 1)
        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 2)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 1)

    def test_area(self):
        rect = Rectangle(5, 3)
        self.assertEqual(rect.area(), 15)

    def test_str(self):
        rect = Rectangle(5, 3, 2, 4, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/4 - 5/3")

    def test_update(self):
        rect = Rectangle(5, 3, 2, 4, 1)
        rect.update(2, 6, 4, 3, 5)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 5)


if __name__ == '__main__':
    unittest.main()
