#!/usr/bin/python3

"""
An BaseGeometry class
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height

    def validate(self):
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
