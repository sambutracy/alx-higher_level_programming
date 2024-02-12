#!/usr/bin/python3
"""
Module defining the Base class.
"""


class Base:
    """
    Base class for managing id attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int):id for the instance. If None, increments __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
