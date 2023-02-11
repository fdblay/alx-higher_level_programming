#!/usr/bin/python3
# 7-base_geometry.py
"""Class BaseGeometry, defines a base geometry"""


class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Value validator
        Args:
            name (str): name of value
            value (int): value to be validated
        Raise:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        self.name = name
        self.value = value
        if value is not int:
            raise TypeError("<self.name> must be an integer".format(self.name))
        if value is <= 0:
            raise ValueError("<self.name> must be greater than 0".format(self.name))
