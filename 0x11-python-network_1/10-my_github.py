#!/usr/bin/python3
"""The script does the following:
 - Takes github credentials
 - Displays github id
"""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = f'https://api.github.com/user'
    auth = HTTPBasicAuth(sys.argv[1], sys.ergv[2])

    response = requests.get(url, auth=auth)
    user_data = response.json()
    print(user_data.get('id'))
