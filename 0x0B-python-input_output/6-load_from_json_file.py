#!/usr/bin/python3
"""Define a load_from_json_file function"""


import json
def load_from_json_file(filename):
    """creates an object from a json file.

    Args:
        filename: the name of the file.
    """

    with open(filename, 'r') as filename:
        obj = json.load(filename)
        return obj
