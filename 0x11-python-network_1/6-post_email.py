#!/usr/bin/python3
"""A script that does the following:
- Takes url and an email as arguments
- Sends a POST request url with the email as a parameter
- Displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    info = {"email": sys.argv[2]}

    r = requests.post(url, data=info)
    print(r.text)
