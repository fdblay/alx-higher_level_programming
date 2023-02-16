#!/usr/bin/python3
"""Python Input_Output, ALX Task-0, 0-read_file.py"""


def read_file(filename=""):
    """Function reads a textfile (UTF8) and prints it to stdout
    Args:
        filename (str): The name of the file to read from
    Returns:
        prints to stdout
    """
    with open(filename, encoding='UTF-8') as r_file:
        print(r_file.read(), end="")
