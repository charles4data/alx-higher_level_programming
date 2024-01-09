#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        greatest = 0
        for number in my_list:
            if number > greatest:
                greatest = number
            else:
                greatest = greatest
    return greatest
