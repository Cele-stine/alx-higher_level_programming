#!/usr/bin/python3
"""This is a base class for the rest of the classe to be created."""


import json
import csv
import turtle

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save instances to a CSV file."""

        filename = f"{cls.__name__}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load instances from a CSV file."""

        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        id, width, height, x, y = map(int, row)
                        instance = cls(width, height, x, y, id)
                    elif cls.__name__ == 'Square':
                        id, size, x, y = map(int, row)
                        instance = cls(size, x, y, id)
                    instances.append(instance)
        except FileNotFoundError:
            pass

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module."""
        # Initialize the Turtle screen
        turtle.title("Drawing Rectangles and Squares")
        screen = turtle.Screen()
        screen.setup(width=800, height=600)
        t = turtle.Turtle()

        # Function to draw a rectangle
        def draw_rectangle(rect):
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)

        # Function to draw a square
        def draw_square(square):
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        # Draw rectangles
        for rect in list_rectangles:
            draw_rectangle(rect)

        # Draw squares
        for square in list_squares:
            draw_square(square)

        # Close the Turtle graphics window on click
        screen.exitonclick()

