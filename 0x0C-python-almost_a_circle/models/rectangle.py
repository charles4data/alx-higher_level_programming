#!/usr/bin/python3

"""
A subclass of Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    Inherits from base class and defines a rectangle
    Adds attributes width, height, x and y
    Defines getters and setters for each attribute, except id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for retrieving the value of width attribute
        self: Instance object
        return: width value of instance object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width, integrating validation methods
        self: Instance object
        value: new value for width, to be updated
        raises:
            TypeError: if value is not an integer
            ValueError: if value is zero or negative
        return: Nothing, only updates the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    # Getter and setter methods for height
    @property
    def height(self):
        """
        Getter method for retrieving the value of the height attribute
        self: Instance object
        return: height value of instance object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height, integrating validation methods
        self: Instance object
        value: new value for height, to be updated
        raises:
            TypeError: if value is not an integer
            ValueError: if value is zero or negative
        return: Nothing, only updates the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    # Getter and setter methods for x
    @property
    def x(self):
        """
        Getter method for retrieving the value of the x
        self: Instance object
        return: x value of instance object
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x, integrating validation methods
        self: Instance object
        value: new value for x, to be updated
        raises:
            TypeError: if value is not an integer
            ValueError: if value is zero or negative
        return: Nothing, only updates the x value
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    # Getter and setter methods for y
    @property
    def y(self):
        """
        getter method for retrieving value of y
        self: Instance object
        return: returns value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y, integrating validation methods
        self: Instance object
        value: new value for x, to be updated
        raises:
            TypeError: if value is not an integer
            ValueError: if value is zero or negative
        return: Nothing, only updates the y value
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculates and returns area of a rectangle instantiated from this class
        return: Area of rectangle object
        """
        return self.height * self.width

    def display(self):
        """
        Prints the area of a Rectangle object using #
        return: returns nothing, just prints
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Prints the Rectangle instance with # for x and y
        Returns the string representation of a rectangle object
        return: Rectangle string presentation
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args):
        """
        Assigns each argument to the corresponding attributes
        args: command line arguments
        return: returns nothing
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
