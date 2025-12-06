#!/usr/bin/python3
"""Create and populate SQLite database."""

import sqlite3


def create_database():
    """Create products database with sample data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear existing data and insert sample data
    cursor.execute('DELETE FROM Products')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Desk Chair', 'Furniture', 249.99),
        (4, 'Wireless Mouse', 'Electronics', 29.99),
        (5, 'Notebook', 'Office Supplies', 9.99)
    ''')
    
    conn.commit()
    
    # Verify data
    cursor.execute('SELECT COUNT(*) FROM Products')
    count = cursor.fetchone()[0]
    print(f"Database created with {count} products")
    
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    print("Products in database:")
    for row in rows:
        print(f"  ID: {row[0]}, Name: {row[1]}, Category: {row[2]}, Price: ${row[3]}")
    
    conn.close()


if __name__ == '__main__':
    create_database()
