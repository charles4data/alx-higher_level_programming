#!/usr/bin/python3

import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_to_list_and_save(args):
    # Check if the file exists, if not create one
    if not path.exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    # Load existing list from file
    items = load_from_json_file("add_item.json")

    # Add new items to the list
    items.extend(args)

    # Save the updated list to the file
    save_to_json_file(items, "add_item.json")


if __name__ == "__main__":
    # Exclude the first argument which is the script name
    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments provided.")
    else:
        add_to_list_and_save(args)

