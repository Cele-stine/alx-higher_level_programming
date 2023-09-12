#!/usr/bin/python3
"""Define save_to_json function."""


import json
def save_to_json_file(my_obj, filename):
    """write an object asto a texfile using json."""
    with open(filename, 'w') as filename:
        obj = json.dump(my_obj, filename)
        return obj
