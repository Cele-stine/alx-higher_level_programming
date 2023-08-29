#!usr/bin/python3
"""Add a Private Attrinbute to the class Square"""
class Square:
    def __init__(self, size):
          """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
