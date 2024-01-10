#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary
    if key not in new_dict:
        new_dict[key] = value
    else:
        new_dict[key] = value
    return new_dict
