#!/usr/bin/python3


"""
Checks if an object is an instance of a certain class
"""


def is_same_class(obj, a_class):
    """
    Returns true of obj is an instance of a_class, otherwise false
    obj: Object instance
    a_class: Class
    return: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
