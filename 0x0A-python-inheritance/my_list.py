#!/usr/bin/python3

"""
A class that inherits and defines a method
"""


class MyList(list):
    """
    class MyList inherits from base class list.
    After inheriting, it defines a method that prints sorted list
    """
    def print_sorted(self):
        print(sorted(self))
