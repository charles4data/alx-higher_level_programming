#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse = my_list[::-1]
    for i in range(len(my_list)):
        print("{:d}".format(reverse[i]))
