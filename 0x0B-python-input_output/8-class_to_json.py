#!/usr/bin/python3
"""Defines the function class_to_json(...)"""


def class_to_json(obj):
    """returns the dictonary description with sample data structure
    for JSON serialization of an object"""
    return obj.__dict__
