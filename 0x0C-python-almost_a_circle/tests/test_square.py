#!/usr/bin/python3

import unittest
from models import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        square = Square(5, 2, 4, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 1)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_str(self):
        square = Square(5, 2, 4, 1)
        self.assertEqual(str(square), "[Square] (1) 2/4 - 5")

    def test_update(self):
        square = Square(5, 2, 4, 1)
        square.update(2, 6, 3, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 5)


if __name__ == '__main__':
    unittest.main()
