#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    my_list = list(set_1) + list(set_2)
    my_set = set(my_list)
    for i in my_set:
        if my_list.count(i) == 2:
            new_list.append(i)
    return new_list
