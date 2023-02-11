#!/usr/bin/python3
# 4-inherits_from.py
"""Defines an inheriter class-verifying function."""


def inherits_from(obj, a_class):
    """Verify if an object is an inherited instance of a class.
    Args:
        obj (any): The object to verify.
        a_class (type): The class to match the type of object to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
