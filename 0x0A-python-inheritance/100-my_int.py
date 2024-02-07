#!/usr/bin/python3
"""
Defines a MyInt class that inherits from int with inverted equality operators.
"""

class MyInt(int):
    """Class MyInt that inherits from int"""

    def __eq__(self, other):
        """Override equality operator =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality operator !="""
        return super().__eq__(other)
