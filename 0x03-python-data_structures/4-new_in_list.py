#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at nth position"""
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    temp_list = list(my_list)
    temp_list[idx] = element
    return temp_list
