#!/usr/bin/python3

"""
Prints the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints the first name and last name

    Args:
        first_name: First name to be printed,
        last_name: Last name to be printed,

    return: returns nothing.

    raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
