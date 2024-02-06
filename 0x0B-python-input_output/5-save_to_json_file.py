#!/usr/bin/python3

"""
Save to json file function
"""


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a text file using
    json representation
    my_obj: object to write in text file
    filename: source file name
    return: Nothing, just writes
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
