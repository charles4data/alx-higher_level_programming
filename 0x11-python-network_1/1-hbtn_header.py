#!/usr/bin/python3
"""
The script takes a url and sends a request
Displays the value of the X-Request-Id variable.
"""

import urllib.request
import sys

url = sys.argv[1]

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
