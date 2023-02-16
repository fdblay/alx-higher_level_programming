#!/usr/bin/python3
"""contains the function write_file(...)"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters"""
    with open(filename, "w") as f:
        f.write(text)
        num = 0
        for char in text:
            num += 1
    return num
