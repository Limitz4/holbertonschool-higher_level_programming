#!/usr/bin/python3
"""Gets X-Request-Id header from URL using requests."""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
