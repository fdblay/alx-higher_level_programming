#!/usr/bin/python3
# 9-student.py
"""Defines a Class, Student"""


class Student:
    """Represents an object, student"""

    def __init__(self, first_name, last_name, age):
        """initialising a new student.
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student instance"""
        if type(attrs) is list and all(type(s) is str for s in attrs):
            res = {}
            for key in attrs:
                if key in self.__dict__:
                    res[key] = self.__dict__[key]
            return res
        else:
            return self.__dict__
