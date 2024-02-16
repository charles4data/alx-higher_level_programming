#!/usr/bin/python3

"""
 A class base
"""


class Base:
    """
    This defines a class base.
    Id is assigned provided value, else assigned the objects count
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
