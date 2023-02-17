#!/usr/bin/python3
# 9-student.py
"""Defines a Class, Student"""


class Student():
    """defines an object, student"""

    def __init__(self, first_name, last_name, age):
        """initialising puplic attributes
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """retrieves a dictionary representation of a student instance"""
            return self.__dict__
