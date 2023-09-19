#!/usr/bin/python3
"""This is a base class for the rest of the classe to be created."""


class Base:
    """Class base is created and has a private attribute.

    private class attribute:
        __nb_objects: Keeps track of howmany objects are created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instanciate class base.

        Args:
            id: object identifier.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
