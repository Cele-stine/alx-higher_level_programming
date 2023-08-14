#!/usr/bin/python
def no_c(my_string):
    modified_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            modified_string += char
    return modified_string
