#!/usr/bin/python3

"""
A Student Class
"""


class Student:
    """
    Defines a student's first and last names, and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary of instance attributes
        return: dictionary items
        """
        return vars(self)
