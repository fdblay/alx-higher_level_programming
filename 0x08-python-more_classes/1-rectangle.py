#!/usr/bin/python3
"""1-rectangle, built for ALX/Holberton project 0x08 task 1.
"""


class Rectangle:
    """creating private instance attributes by taking in
    two arguments.
    
    
    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0

    """
    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: if `value` is not an int.
            ValueError: if `value is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangel

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: if `value` is not an int.
            ValueError: if `value` is less than 0.
        
        """
        if type(value) is not int:
            raise TypeError('heigth must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
