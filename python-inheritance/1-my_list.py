#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """MyList class that inherits from list"""
    
    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
