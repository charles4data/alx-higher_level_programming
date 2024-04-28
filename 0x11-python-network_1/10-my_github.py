#!/usr/bin/python3
"""The script does the following:
 - Takes github credentials
 - Displays github id
"""

if __name__ == '__main__':
    import requests
    import sys

    url = f'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.ergv[2]

    response = requests.get(url, auth=(username, token))
    user_data = response.json()
    print(user_data.get('id'))
