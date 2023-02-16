#!/usr/bin/python3
"""Defines a module that contains the function save_to_json_file(...)
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a textfile, using a JSON representation."""
    with open(filename, "w", encoding='utf-8') as f:
        return json.dump(my_obj, f)
