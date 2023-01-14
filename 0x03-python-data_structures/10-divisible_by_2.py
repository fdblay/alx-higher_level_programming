#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list"""
    if not my_list:
        return my_list
    new_list = list(my_list)
    for index in new_list:
        if index % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
    return new_list
