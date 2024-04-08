#!/usr/bin/python3
"""
A function that prints 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    # Checking if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define characters that trigger new lines
    new_line_chars = ['.', '?', ':']

    for char in text:
        if char not in new_line_chars:
            print(char, end='')
        else:
            print(char)
            print()

    print()
