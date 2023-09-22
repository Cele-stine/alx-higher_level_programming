#!/usr/bin/python3
"""This is a base class for the rest of the classe to be created."""


import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries.

        Args:
            list_dictionaries: a list of dictionaries.

        Return: Json string or an empty list if list_dictionaries is empty.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_obgs to a file.

        Args:
            list_obgs: a list if instances who inherit frim the base.
        """

        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_objs = []

        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dict)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    def from_json_string(json_string):
        """Return a list from the JSON string representation json_string.

        Args:
            json_string: a string representing a list of dintionaries.
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
