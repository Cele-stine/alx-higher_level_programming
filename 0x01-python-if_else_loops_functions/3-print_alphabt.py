#!/usr/bin/python3
skip = [101, 113]
for char in range(97, 123):
    if char not in skip:
        print("{}".format(chr(char)), end="")
