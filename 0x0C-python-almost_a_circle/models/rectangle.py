#!/usr/bin/python3
"""
Module defining the Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The id for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The value to set as the width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The value to set as the height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The value to set as the x-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The value to set as the y-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the Rectangle instance.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with '#' characters.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: String representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """
        Assigns arguments to attributes in the specified order.

        Args:
            *args: Arguments to assign to the attributes.
                   1st arg: id
                   2nd arg: width
                   3rd arg: height
                   4th arg: x
                   5th arg: y
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
