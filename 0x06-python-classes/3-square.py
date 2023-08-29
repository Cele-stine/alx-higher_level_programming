#!/usr/bin/python3
"""Find the area of a square."""


class Square:
    """Private instance size.

    Args:
    size(int): size of the square.
    """

    def __init__(self, size=0):
        if not isinstance (size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method area."""

        return (self.__size * self.__size)
