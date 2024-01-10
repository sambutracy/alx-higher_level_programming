#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Using list comprehension to create a new dictionary
    new_dict = {key: val for key, val in a_dictionary.items() if val != value}
    return new_dict
