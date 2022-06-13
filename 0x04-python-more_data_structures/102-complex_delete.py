#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    if value not in a_dictionary.values():
        return a_dictionary
    for k, v in a_dictionary.items():
        if v == value:
            del_keys.append(k)
    for key in del_keys:
        del a_dictionary[key]
    return a_dictionary
