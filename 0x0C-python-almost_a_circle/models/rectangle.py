#!/usr/bin/python3
"""Creat class Rectangle that inherits from  Base."""

from models.base import Base

class Rectangle(Base):
    """Define a class than inherits from Base.

    Args:
        Base: Class to inhetit from.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inastanciate the class.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle
            x: Horizontal coordinate from the top left coner of the rectangle.
            y: Vertical coordinate from the top left coner of the rectangle.
            id: Object identifier.
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    #set getter/setter for the attributes.
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height
