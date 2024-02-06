#!/usr/bin/python3

"""
A Read File Function
"""


def read_file(filename=""):
    """
    Reads a file and prints to stdout
    filename: File to be read
    return: returns nothing
    """
    with open(filename, mode="r", encoding='UTF-8') as file:
        info = file.read()
        print(info)
