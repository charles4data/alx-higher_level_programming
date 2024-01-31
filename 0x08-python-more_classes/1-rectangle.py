#!/usr/bin/python3

"""
A rectangle class
"""


class Rectangle:
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance/object

        width: rectangle width
        height: rectangle height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        getter method to retrieve width of the rectangle class

        return: returns the value of the width attribute
        """
        return self.__width

    @property
    def height(self):
        """
        getter method to retrieve the height of the rectangle class

        return: returns the value of the height attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter method for changing value of width attribute

        value: new value of width attribute
        raise:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter method for changing value of height attribute
        value: The new value to be changed to
        raise:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
