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

        Raises:
            TypeError: width, height, x, and y raise a TypeError if not int.
            ValueError: if less or equal to zero width&height raise Valueerr.
            ValueError: If less than zero x&y raise ValueError.
        """

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """Getter/setter for the private attributes."""

    @property
    def width(self):
        """Getter for width."""

        return self.__width

    @width.setter
    def width(self, value):
        """setter for width.

        Args:
            value: The new value to set width to.
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value: The new value to set height to.
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""

        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value: The new value to set x to.
        """

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""

        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

        Args:
            value: The new value to set y to.
        """

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""

        return self.width * self.height

    def display(self):
        """Print the rectangle instance with the character #."""

        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
