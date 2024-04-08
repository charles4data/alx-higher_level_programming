#!/usr/bin/python3

"""
A function that writes a string to a file
"""


def write_file(filename="", text=""):
    """
    Opens a file and writes text into it
    filename: file to write into
    text: text to write into the file
    return: returns length of written text
    """
    with open(filename, mode="w", encoding='utf-8') as file:
        file.write(text)
        return len(text)
