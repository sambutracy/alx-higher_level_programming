#!/usr/bin/python3
""" Defining a class of a square."""

class Square:
    """class to define the square

    Attributes:
        __size (int): Private instance attribute for the size of the square
    """
    def __init__(self,size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
