#!/usr/bin/python3
import copy


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return copy.copy(my_list)
    newlist = copy.deepcopy(my_list)
    newlist[idx] = element
    return newlist
