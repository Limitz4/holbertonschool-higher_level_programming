#!/usr/bin/python3
"""Lookup function module"""


def lookup(obj):
    """Return the list of available attributes and methods of an object
    
    Args:
        obj: The object to inspect
        
    Returns:
        A list of attributes and methods
    """
    return dir(obj)
