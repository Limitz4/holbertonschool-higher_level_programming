#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object."""
    return obj.__dict__
