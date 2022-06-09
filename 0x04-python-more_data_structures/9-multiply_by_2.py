#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    dict_values = a_dictionary.values()
    dict_values = list(map(lambda x: x * 2, dict_values))
    for i, k in enumerate(a_dictionary):
        new_dict[k] = dict_values[i]
    return new_dict
