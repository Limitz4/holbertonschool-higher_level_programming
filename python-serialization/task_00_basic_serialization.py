#!/usr/bin/python3
"""Basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to JSON file"""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
