#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = a_dictionary.keys()
    for key in sorted(my_list):
        print(f"{key}: {a_dictionary[key]}")
