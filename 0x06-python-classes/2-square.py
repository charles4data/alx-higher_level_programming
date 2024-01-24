#!/usr/bin/python3

""" This is a square class """


class Square:
    """This class defines a square
    Attributes: int(size) - means size of a square"""
    def __init__(self, size=0):
        """ The size attribute defines the size of a square
        Arguments: int(size)"""
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")

        if not value >= 0:
            raise ValueError("Size must be greater than or equal to 0")

        self._size = value
