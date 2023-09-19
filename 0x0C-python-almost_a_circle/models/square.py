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
