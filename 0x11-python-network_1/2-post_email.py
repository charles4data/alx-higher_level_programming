#!/usr/bin/python3

"""A Script that does the following:
 - Takes a url and email as arguments,
 - Sends a request to the url using email as parameter,
 - displays the body of the response (decoded in utf-8).
"""


import urllib.request
import sys

url = sys.argv[1]
params = {"email": sys.argv[2]}

request = urllib.request.Request(url, params)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
