#!/usr/bin/python3

"""
An append write function
"""


def append_write(filename="", text=""):
    """
    Appends text and counts characters added
    filename: name of the file to write into
    text: The text to write into file
    return: num of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
