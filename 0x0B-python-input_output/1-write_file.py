#!/usr/bin/python3
"""Define a finction write_file."""


def write_file(filename="", text=""):
    """Write to a file and return the number of char

    Args:
        filename: the name of the file.
        text: the string to write.
    """
    with open(filename, 'w', encoding='utf-8') as filename:
        filename.write(text)
        return len(text)
