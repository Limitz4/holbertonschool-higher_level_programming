#!/usr/bin/python3
"""Sends POST request with letter and processes JSON response."""

import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    
    data = {'q': q}
    r = requests.post(url, data=data)
    
    try:
        json_data = r.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), 
                                   json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
