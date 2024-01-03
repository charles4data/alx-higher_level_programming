#!/usr/bin/python3

def uppercase(str):
    result = ""
    if str is not None:
        for char in str:
            if 'a' <= char <= 'z':
                upper = chr(ord(char) - ord('a') + ord('A'))
                result += upper
            else:
                result += char
    print(result)
