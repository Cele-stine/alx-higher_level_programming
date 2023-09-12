#!/usr/bin/python3
"""Define to_json_string function."""



import json
def to_json_string(my_obj):
    """Return a json representation of an object.

    Args:
        My_obj: the object.
    """

    obj = json.dumps(my_obj)
    return (obj)
