#!/usr/bin/python3

import sys


def add_arguments(arguments):
    return sum(int(arg) for arg in arguments)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    result = add_arguments(arguments)
    print(result)
