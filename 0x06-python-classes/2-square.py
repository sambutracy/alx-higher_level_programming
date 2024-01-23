#!/usr/bin/python3
class Square:
    """Square class represents a square.

    Attributes:
        __size (int): Private instance attribute for the size of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
