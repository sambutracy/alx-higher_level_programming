#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size):
        """Initialize the Square with size"""
        super().__init__(size, size)

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
