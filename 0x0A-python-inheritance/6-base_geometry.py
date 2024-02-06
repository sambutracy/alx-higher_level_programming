#!/usr/bin/python3
"""the class raises error when it's empty"""


class BaseGeometry:
    """Base class for geometry."""
    
    def area(self):
        """Raise an Exception error message"""
        raise Exception("area() is not implemented")
