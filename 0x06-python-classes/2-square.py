#!/usr/bin/python3

""" This is a square class """


class Square:
    """This class defines a square
    Attributes: int(size) - means size of a square"""
    def __init__(self, size=0):
        """ The size attribute defines the size of a square
        Arguments: int(size)"""
        assert size == int, "Size must be an integer"
        assert size >= 0, "size must be >= 0"

        # instantiate size
        self._size = size

