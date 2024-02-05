#!/usr/bin/python3

"""
Function that lists class attributes and methods
"""


def lookup(obj):
    """
    Lists the methods and attributes available in a class
    obj: class object
    return: List of all attributes and methods
    """
    return dir(obj)
