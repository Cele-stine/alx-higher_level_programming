#!/usr/bin/python3
"""Define from_json_string function."""


import json
def from_json_string(my_str):
    """A function that returns an object representesd by json string.

    Args:
        My_str: the string.
    """

    string = json.loads(my_str)
    return (string)
