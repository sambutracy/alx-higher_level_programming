#!/usr/bin/python3
"""Script to add arguments to a Python list and save them to a JSON file"""
import sys
import json
from os import path

# Importing the custom functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Filename for the JSON file
filename = 'add_item.json'

# Create an empty list if the file doesn't exist, otherwise load the list from the file
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Adding command line arguments to the list
my_list.extend(sys.argv[1:])

# Saving the updated list to the JSON file
save_to_json_file(my_list, filename)
