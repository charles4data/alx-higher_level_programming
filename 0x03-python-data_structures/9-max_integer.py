#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        maxm = my_list[0]
        for number in my_list:
            if number > maxm:
                maxm = number
            else:
                maxm = maxm
    return maxm
