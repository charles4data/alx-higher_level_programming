#!/usr/bin/python3

"""
Load an object from json function
"""


def load_from_json_file(filename):
    """
    Creates an object from a jason file
    filename: must be the json file
    return: returns the object
    """
    import json
    with open(filename, mode='r', encoding='utf-8') as file:
        my_obj = json.load(file)
        return my_obj
