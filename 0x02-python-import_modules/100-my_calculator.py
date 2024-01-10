#!/usr/bin/python3

# import needed functions and modules
from calculator_1 import add, sub, mul, div
import sys

# define function
if __name__ == '__main__':
    def calculate_arguments():
        args = sys.argv[1:]

        if len(args) != 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
        elif args[1] != '+' and args[1] != '-' and args[1] != '*' and args[1] != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            a = int(args[0])
            b = int(args[2])
            operator = args[1]

            if operator == '+':
                print(f'{a} + {b} = {add(a, b)}')
            elif operator == '-':
                print(f'{a} - {b} = {sub(a, b)}')
            elif operator == '*':
                print(f'{a} * {b} = {mul(a, b)}')
            elif operator == '/':
                print(f'{a} / {b} = {div(a, b)}')


    calculate_arguments()
