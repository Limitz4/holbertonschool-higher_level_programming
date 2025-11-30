#!/usr/bin/python3
"""Convert CSV to JSON"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON file"""
    try:
        # Read CSV and convert to list of dictionaries
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)
        
        # Write JSON data to file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
