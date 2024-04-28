#!/usr/bin/python3
"""
This script does the following:
 - Takes url and email as arguments,
 - Sends a POST request to the passed URL, and
 - displays the body of the response (decoded in utf-8)
 """

import urllib.parse
import urllib.request
import sys


url = sys.argv[1]
data = {"email": sys.argv[2]}

request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
