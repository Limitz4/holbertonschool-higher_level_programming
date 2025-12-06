#!/usr/bin/python3
"""Lists 10 recent GitHub commits."""

import sys
import requests


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    
    r = requests.get(url, params={'per_page': 10})
    commits = r.json()
    
    if type(commits) is list:
        for commit in commits:
            sha = commit.get('sha')
            name = commit.get('commit', {}).get('author', {}).get('name')
            print("{}: {}".format(sha, name))
