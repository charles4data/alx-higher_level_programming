#!/usr/bin/python3
"""A script that:
 - fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
	import requests

	url = 'https://alx-intranet.hbtn.io/status'
	html = requests.get(url)

	print("Body Response:")
	print("\t- type: {}".format(html.text.__class__))
	print("\t- content: {}".format(html.text))
