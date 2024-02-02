#!/usr/bin/python3


"""
Function that prints size of a square as #
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print('#' * size)
