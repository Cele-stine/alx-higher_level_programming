#!/usr/bin/python3
"""Add property getter and property setter."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Instantiate size.

        Args:
        size(int): the size of a square Square.
        """

        self.__size = size

    @property
    def size(self):
        """Getter for property size."""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Change the property size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        """Calculate the area of the square"""

        return (self.__size * self.__size)
