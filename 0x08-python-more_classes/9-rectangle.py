#!/usr/bin/python3

"""
A rectangle class
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    """
    defines a rectangle
    """
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

    def area(self):
        """
        returns the area of an instance
        return: returns area * height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of a rectangle
        return: 2 * height + 2 * width
        """
        if self.__height == 0 and self.__width == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        returns area represented as # or 0 or either height or width is 0
        """
        if self.__height == 0 or self.__width == 0:
            return f""
        else:
            return '\n'.join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """
        returns string representations of rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor method called when rectangle object is about to be destroyed
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle....")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A static method that Compares rect_1 and rect_2 and returns the biggest one
        rect_1: The first rectangle - an instance of Rectangle class
        rect_2: The second rectangle - also an instance of the Rectangle class
        return: Returns the biggest rectangle or rect_1 if the areas of both are the same
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a rectangle instance with height == width == size.
        size: The size of the square, default is zero
        return: A new rectangle instance representing a square
        """
        return cls(size, size)
