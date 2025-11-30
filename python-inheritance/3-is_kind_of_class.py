#!/usr/bin/python3
"""
Function to check if object is instance of specified class or inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is instance of a_class or inherited from a_class
    """
    return isinstance(obj, a_class)
