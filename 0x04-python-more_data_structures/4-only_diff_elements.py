#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    if len(set_1) <= len(set_2):
        small_set = set_1
        big_set = set_2
    else:
        small_set = set_2
        big_set = set_1
    for i in big_set:
        if i not in small_set:
            my_list.append(i)
    return my_list
