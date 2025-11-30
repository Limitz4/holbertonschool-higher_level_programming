#!/usr/bin/python3
"""
Function to check if object inherits from specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj inherits from a_class (directly or indirectly)
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
