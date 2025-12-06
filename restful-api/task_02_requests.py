#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API.
"""

import csv
import requests


def fetch_and_print_posts():
    """Fetch and print posts."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f'Status Code: {r.status_code}')
    
    if r.status_code == 200:
        data = r.json()
        for item in data:
            print(item.get('title'))


def fetch_and_save_posts():
    """Fetch and save posts to CSV."""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if r.status_code == 200:
        data = r.json()
        posts = []
        
        for item in data:
            posts.append({
                'id': item.get('id'),
                'title': item.get('title'),
                'body': item.get('body')
            })
        
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts)
