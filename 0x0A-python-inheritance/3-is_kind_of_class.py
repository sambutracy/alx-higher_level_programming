#!/usr/bin/python3
"""function to check the class and inheritance of an object"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or inherited from specified class."""
    return isinstance(obj, a_class)
