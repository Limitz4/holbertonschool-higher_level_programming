#!/usr/bin/python3
"""
Flask application with dynamic template and logic.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Load items from JSON file."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []


@app.route('/')
def home():
    """Home page."""
    return "Welcome to the Items App. Go to /items to see the items list."


@app.route('/items')
def items():
    """Display items list."""
    items_list = load_items()
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
