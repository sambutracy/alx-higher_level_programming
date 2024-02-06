#!/usr/bin/python3
"""function to check subclass of an object"""


def inherits_from(obj, a_class):
    """Check if obj is subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
