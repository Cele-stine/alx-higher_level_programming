#!/usr/bin/python3
"""Define a class Square that inherits from the Rectangle class."""


from models.rectangle import Rectangle

class Square(Rectangle):
    """A class defining a square that inherits attributes from Rectangle."""


    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation of Square.

        Args:
           size: The length of the side of square.
           x: Coordinate of square from the left top, right to left.
           y: Coordinate fo square from the left top, top to bottom.
           id: the Object identifies.
        """

        super().__init__(size, size, x, y , id)

    def __str__(self):
        """User Readable string representation of square."""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size."""

        return self.width

    @size.setter
    def size(self, value):
        """setter for size.

        Args:
            value: the value to set size to.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square by adding *args and **kwargs.

        Args:
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments.
        """

        if args:
            # If *args is not empty, assign attributes from args
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            # If *args is empty, assign attributes from kwargs
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of Square."""

        return {
                'id' : self.id,
                'size' : self.width,
                'x' : self.x,
                'y' :self.y
                }
