#!/usr/bin/python3
#1-my_list.py
"""Defines an inherited list class MyList."""


class MyList(list):
    """Initiates sorted printing for built-in list class."""

    def print_sorted(self):
        """Print a list sorted in ascending order."""
        print(sorted(self))
