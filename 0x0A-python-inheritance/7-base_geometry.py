#!/usr/bin/python3

"""
An BaseGeometry class
"""


class BaseGeometry:
    """
    Area method defined for this class
    integer_validator defined also
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
