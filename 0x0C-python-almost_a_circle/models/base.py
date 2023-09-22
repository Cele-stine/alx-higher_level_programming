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

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with attributes set from the dictionary.

        Args:
            **dictionary: Keyword argument.
        """

        if cls.__name__ == 'Rectangle':
            instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            instance = cls(1)  # Create a dummy Square instance

        instance.update(**dictionary)  # Use the update method to assign attributes
        return instance

    @classmethod
    def load_from_file(cls):
        """Load and return a list of instances from a JSON file."""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**data) for data in list_dicts]
        except FileNotFoundError:
            return []
