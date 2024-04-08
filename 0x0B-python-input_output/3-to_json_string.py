#!/usr/bin/python3

"""
serializes objects into json notation
"""


def to_json_string(my_obj):
    """
    returns the json representation of an object
    my_obj: object tp jsonify
    return: json representation
    """
    import json
    return json.dumps(my_obj)
