#!/usr/bin/python3
"""GitHub API user id."""

import sys
import requests


if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(u, p))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")
