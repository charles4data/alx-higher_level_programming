#!/usr/bin/python3

def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0 or idx >= size:
        print("None")
    else:
        for i in my_list:
            if i == idx:
                return my_list[idx]
