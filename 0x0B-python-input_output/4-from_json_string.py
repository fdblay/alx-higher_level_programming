#!/usr/bin/python3
"""Defines the function from_json_string(...)"""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object(sring)"""
    return json.loads(my_str)
