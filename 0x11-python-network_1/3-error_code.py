#!/usr/bin/python3
"""The script does the following:
 - takes in a URL,
 - sends a request to the URL, and
 - displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    url = sys.argv[1]

    try:
        with request.urlopen(url) as r:
            print(r.read().decode('UTF-8'))
    except error.HTTPError as e:
        print('Error code:', e.code)
