#!/usr/bin/python3

"""A Script that does the following"""


import urllib.request
import sys

url = sys.argv[1]
params = {"email": sys.argv[2]}

request = urllib.request.Request(url, params)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
