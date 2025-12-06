#!/usr/bin/python3
"""
Flask application for displaying products from JSON, CSV, or SQLite database.
"""

import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    """Read and parse JSON file."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return []


def read_csv_file():
    """Read and parse CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except (FileNotFoundError, KeyError, ValueError) as e:
        return []
    return products


def read_sqlite_database():
    """Read products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products ORDER BY id')
        
        rows = cursor.fetchall()
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    
    return products


@app.route('/products')
def display_products():
    """Display products from JSON, CSV, or SQLite database."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id', type=int)
    
    # Read data based on source
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    elif source == 'sql':
        products = read_sqlite_database()
    else:
        return render_template('product_display.html', 
                             error=f"Wrong source: '{source}'. Use 'json', 'csv', or 'sql'.",
                             source=source)
    
    # Filter by ID if provided
    if product_id:
        filtered_products = [p for p in products if p['id'] == product_id]
        if not filtered_products:
            return render_template('product_display.html',
                                 error=f"Product with ID {product_id} not found",
                                 source=source,
                                 product_id=product_id)
        products = filtered_products
        info = f"Showing product ID {product_id}"
    else:
        info = f"Showing all {len(products)} products" if products else None
    
    return render_template('product_display.html',
                          products=products,
                          source=source,
                          info=info,
                          product_id=product_id)


@app.route('/')
def home():
    """Home page with instructions."""
    return '''
    <h1>Products Display Application</h1>
    <p>Available sources: json, csv, sql</p>
    <p>Examples:</p>
    <ul>
        <li><a href="/products?source=json">All JSON products</a></li>
        <li><a href="/products?source=csv">All CSV products</a></li>
        <li><a href="/products?source=sql">All SQL database products</a></li>
        <li><a href="/products?source=sql&id=1">SQL product ID 1</a></li>
    </ul>
    '''


if __name__ == '__main__':
    app.run(debug=False, port=5000)
