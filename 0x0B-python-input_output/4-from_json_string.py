#!/usr/bin/python3

"""
From json to String Function
"""


def from_json_string(my_str):
    """
    Deserializes into a python object
    my_str: json string
    return: python object
    """
    import json
    return json.loads(my_str)
