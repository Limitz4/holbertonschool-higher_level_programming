#!/usr/bin/python3
"""GitHub commits."""

import sys
import requests


if __name__ == "__main__":
    r = requests.get("https://api.github.com/repos/{}/{}/commits"
                     .format(sys.argv[2], sys.argv[1]))
    j = r.json()
    for c in j[:10]:
        print("{}: {}".format(c['sha'], c['commit']['author']['name']))
