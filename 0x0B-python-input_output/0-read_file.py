#!/usr/bin/python3
"""Define a function that reads a file and prints its content."""


def read_file(filename=""):
    """Open file to read.

    Args:
    filename: the name assigment of the file while opening.
    """

    with open(filename, 'r', encoding='utf-8') as filename:
        lines = filename.read()
        print(lines)
