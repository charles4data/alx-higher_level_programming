#!/usr/bin/python3
"""The script does the following:
 - Takes a repository and its owner
 - lists the 10 most recent commits .
"""

if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    user = sys.argv[2]

    url = f"https://api.github.com/repos/{user}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
