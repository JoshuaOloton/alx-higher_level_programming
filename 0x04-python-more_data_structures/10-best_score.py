#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_value = 0
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    position = val_list.index(max_value)
    key_value = key_list[position]
    return key_value
