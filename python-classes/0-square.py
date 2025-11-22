#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Square class with private size attribute"""
    
    def __init__(self, size):
        """Initialize square with size
        
        Args:
            size: size of the square
        """
        self.__size = size
