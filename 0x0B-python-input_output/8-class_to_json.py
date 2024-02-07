#!/usr/bin/python3
"""return dictionary description with simple data strcture"""


def class_to_json(obj):
    """Converts an object of a class to a dictionary description for JSON serialization"""
    # Getting the dictionary of object attributes
    obj_dict = obj.__dict__.copy()

    # Handling the case where class attributes are also serialized
    if hasattr(obj, '__dict__'):
        obj_dict.update(obj.__dict__)

    # Removing any attributes starting with '__' which are considered private
    for key in list(obj_dict.keys()):
        if key.startswith('__'):
            del obj_dict[key]

    return obj_dict
