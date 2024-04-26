#!/usr/bin/python3

"""The script fetches content from the link"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        url_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(url_content)))
        print("\t- content: {}".format(url_content))
        print("\t- utf8 content: {}".format(url_content.decode('utf-8')))
