#!/usr/bin/python3

if __name__ == "__main__":
    # importing modules
    from calculator_1 import sub, add, mul, div

    # assigning variables
    a = 10
    b = 5

    # printing results
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

