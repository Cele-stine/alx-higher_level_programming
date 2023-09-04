#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialise Rectangle.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    """Setter for width.

    Args:
    value: the value assigned to the with of the rectangle.
    """
    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    """Setter for height.

    Args:
    value: the value assigned to the with of the rectangle.
    """
    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
