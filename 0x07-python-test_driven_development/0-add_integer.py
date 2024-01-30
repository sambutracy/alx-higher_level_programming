#!/usr/bin/python3
"""
Module for a function adding two integers.

This module contains the add_integer function, which takes two arguments, a and b, and returns their sum as an integer. If either a or b is a float, it will be cast to an integer before performing the addition.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: an integer or float
    - b: an integer or float (default is 98)

    Returns:
    - The addition of a and b as an integer.

    Raises:
    - TypeError: If a or b is not an integer or float.
    """

    # Check if a is not an integer or float
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    # Check if b is not an integer or float
    if type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b
