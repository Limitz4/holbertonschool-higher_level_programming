#!/usr/bin/python3
"""
Takes in a URL, sends a request and displays X-Request-Id header
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
