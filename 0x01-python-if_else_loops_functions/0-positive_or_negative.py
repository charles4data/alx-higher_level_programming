#!/usr/bin/python3

import random

number = random.randint(-100, 100)

if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
