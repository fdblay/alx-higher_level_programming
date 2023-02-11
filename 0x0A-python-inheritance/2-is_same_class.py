#!/usr/bin/python3
#2-is_same_class.py
"""Defines a class verification function"""


def is_same_class(obj, a_class):
    """Verify if object is exactly an instance of a given class.
    Args:
        obj (any): The object to verify
        a_calss (type): The class to match the type of obj to.

    Return:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
