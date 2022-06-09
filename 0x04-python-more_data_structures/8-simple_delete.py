#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_dict = {}
    for k, v in a_dictionary:
        if k != key:
            new_dict[k] = v
    return new_dict
