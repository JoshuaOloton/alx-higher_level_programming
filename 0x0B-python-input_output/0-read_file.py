#!/usr/bin/python3

''' defines a function that reads a textfile '''


def read_file(filename=""):
    ''' read a textfile and print to stdout '''
    with open(filename, encoding='utf-8') as file:
        print(file.read())
