#!/usr/bin/python3
"""Python Input_Output, ALX Task-0, "1-write_file.py"""


def write_file(filename="", text=""):
    """Function writes a string to a textfile (UTF8)
    Args:
        filename (str): The name of the file to read from
        text (str): The string to be written
    Returns:
        the number of characters written
    """
    with open(filename,"w") as w_file:
        num_of_chars = w_file.write(text)
    return num_of_chars
