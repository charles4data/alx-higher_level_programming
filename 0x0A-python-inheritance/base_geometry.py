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
        """
        Validates values given
        name: key
        value: integer associated with the key
        return: TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
