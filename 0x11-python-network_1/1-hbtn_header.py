#!/usr/bin/python3
""" The script takes a url and displays x-request-id"""

import urllib.request
import sys


url = sys.argv[1]

request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
