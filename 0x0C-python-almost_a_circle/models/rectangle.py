#!/usr/bin/python3

from models.base import Base

"""
A subclass of Base class
"""


class Rectangle(Base):
    """
    Inherits from base class and defines a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        # Getter and setter methods for width
        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        # Getter and setter methods for height
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        # Getter and setter methods for x
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        # Getter and setter methods for y
        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value