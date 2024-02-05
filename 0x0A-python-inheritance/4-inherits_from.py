#!/usr/bin/python3

"""
Checking whether an obj is an instance of a class, which is only a subclass of another class
"""


def inherits_from(obj, a_class):
    """
    Function checks whether obj is an instance of a class, which inherits from a_class
    obj: instance object
    a_class: the parent class or base class
    return: True or False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
