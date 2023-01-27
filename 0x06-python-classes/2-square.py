#!/usr/bin/python3
"""Class Square"""

class Square:
    """Defines a square with
    - private instance attribute: size
    - and instantiation with optional 
    - size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """size is a private attribute:
        - size must be an integger, otherwise raise a 'TypeErro'
        exception with the message size must be an integer
        - if size is less than 0, raise a ValueError exception
        with the message size must be >= 0"""
        
        if(type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size
