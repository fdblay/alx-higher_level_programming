#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """Representation of inheriting class
    """

    def __eq__(self, value):
        """Magic method equals
        """

        return super().__ne__(value)

    def __ne__(self, value):
        """Magic method not equals
        """

        return super().__eq__(value)
