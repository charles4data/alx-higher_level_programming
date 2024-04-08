#!/usr/bin/python3
def search_replace(my_list, search, replace):
    size = len(my_list)
    if size != 0 and search is not None and replace is not None:
        new_list = my_list.copy()
        for i in range(size):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list
