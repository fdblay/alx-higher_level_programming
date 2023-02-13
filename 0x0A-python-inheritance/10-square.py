#!/usr/bin/python3
# 10-square.py
"""Defines a class Square that inherits from class Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using Rectangle."""

    def __init__(self, size):
        """Instantiation size of square.
        Args:
            size (int): determines how big or small the square is
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method returns the area of the square.
        """

        return self.__size * self.__size
