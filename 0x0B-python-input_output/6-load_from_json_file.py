#!/usr/bin/python3
"""creates an object from a json file"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, 'r')as json_file:
        temp=json.loads(json_file.read())
    return temp
