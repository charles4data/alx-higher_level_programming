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

    @staticmethod
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def validate(self):
        BaseGeometry.integer_validator("width", self.__width)
        BaseGeometry.integer_validator("height", self.__height)
