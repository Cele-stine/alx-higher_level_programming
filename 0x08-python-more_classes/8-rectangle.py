#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represents a rectangle.

    Attributes: 
        number_of_attributes: keeps count of  the number of instances in the class.
        print_symbol: used as a symbol for string representation.
    """


    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height


        #when a new Rectangle is created, Number_of_instances is incremented.

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter\setter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter\seter for height."""
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle."""
        return (self.__width * self.__height)
    def perimeter(self):
        """Finding the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Returns a rectangle representation, printed by character '#'."""

        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    def __del__(self):
        """print a massage for every deletion of a rectangle"""
        print("Bye rectangle...")

        #When a rectangle is deleted, decrement.

        Rectangle.number_of_instances -= 1
