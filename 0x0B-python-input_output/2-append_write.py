#!/usr/bin/python3
"""Define a function append_write."""


def append_write(filename="", text=""):
    """Append a string to a file.

    Args:
        filename: the file
        text: the string to append.
    """

    with open(filename, 'a', encoding='utf-8') as filename:
        filename.write(text)
        return len(text)
