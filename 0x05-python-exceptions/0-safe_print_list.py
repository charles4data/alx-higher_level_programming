#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0
    for _ in my_list:
        count += 1

    length = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            length += 1

    except IndexError:
        pass

    print()
    return length
