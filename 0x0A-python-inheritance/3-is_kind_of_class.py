#!/usr/bin/python3

"""
Function that checks if an object is an instance of a class or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or instance of subclass of a-class
    obj: Instance object to be checked
    a_class: class or base class from where obj was instantiated from
    return: True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
