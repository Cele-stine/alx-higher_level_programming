#!/usr/bin/python3
"""Print in stdout the area of rge square with '#' character"""


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

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""

        return (self.__size * self.__size)
    
    def my_print(self):
        """Print the '#' character."""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print ("")
        if self.size == 0:
            print("")
