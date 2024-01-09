#!/usr/bin/python3

def element_at(my_list, idx):
    size = len(my_list)
    if 0 > idx or idx >= size:
        return None
    else:
        for i in my_list:
            return my_list[idx]
