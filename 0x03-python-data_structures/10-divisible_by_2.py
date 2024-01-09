#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        new_list = my_list[:]
        for num in new_list:
            if num % 2 == 0:
                new_list[num] = True
            else:
                new_list[num] = False
        return new_list
