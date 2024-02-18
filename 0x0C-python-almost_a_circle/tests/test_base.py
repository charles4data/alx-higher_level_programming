#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_init_without_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_from_json_string_empty(self):
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_to_json_string_empty(self):
        list_dictionaries = []
        result = Base.to_json_string(list_dictionaries)
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        list_dictionaries = None
        result = Base.to_json_string(list_dictionaries)
        self.assertEqual(result, "[]")


if __name__ == '__main__':
    unittest.main()
