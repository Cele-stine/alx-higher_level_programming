#!/usr/bin/python3
"""Define class_to_json function."""


def class_to_json(obj):
    """A function that returns the dictionary discription with simple DS.

    Args:
        obg: the object to json serialize.
    """

    if isinstance(obj, dict):
        return {key : class_to_json(value) for key, value in obj.item()}
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, (int, str, bool)):
        return obj
    elif isinstance(obj, object):
        attributes = {}
        for attr_name in dir(obj):
            # Exclude private attributes and methods.
            if not attr_name.startswith("_"):
                attr_value = getattr(obj, attr_name)
                # Recursively serialize the attribute.
                attributes[attr_name] = class_to_json(attr_value)
        return attributes
    else:
        # Raise an exception if the object is of an unsupported type.
        raise TypeError(f"Unsupported type: {type(obj)}")
