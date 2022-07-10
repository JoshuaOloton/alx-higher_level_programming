#!/usr/bin/python3

''' defines function to print firstname and lastname '''


def say_my_name(first_name, last_name=""):
    if not type(first_name) == str:
        raise TypeError('first_name must be a string')
    if not type(last_name) == str:
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
