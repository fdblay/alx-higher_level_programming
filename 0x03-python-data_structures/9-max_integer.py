#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if not my_list or len(my_list) == 0:
        return None
    biggest = my_list[0]
    for index in my_list:
        if index > biggest:
            biggest = index
    return biggest
