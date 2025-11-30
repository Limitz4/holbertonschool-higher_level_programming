#!/usr/bin/python3
"""
BaseGeometry class with area and integer_validator methods
"""


class BaseGeometry:
    """BaseGeometry class with validation methods"""
    
    def area(self):
        """Raises Exception that area is not implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
