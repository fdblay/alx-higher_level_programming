#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order"""
    if not my_list:
        return None
    my_list.reverse()
    for index in my_list:
        print('{:d}'.format(index))
