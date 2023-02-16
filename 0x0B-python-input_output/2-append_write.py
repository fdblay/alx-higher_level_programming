#!/usr/bin/python3
"""contains the function append_file(...)"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8) and
    returns the number of characters"""
    with open(filename, "a") as f:
        f.write(text)
        num = 0
        for char in text:
            num += 1
    return num
