#!/usr/bin/python3
"""Takes url and email, and displays response body"""

import urllib.parse
import urllib.request
import sys


url = sys.argv[1]
data = {"email": sys.argv[2]}

request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    print(response.read().decode("utf-8"))
