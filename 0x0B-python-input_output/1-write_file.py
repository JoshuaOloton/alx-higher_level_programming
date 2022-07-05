#!/usr/bin/python3

''' defines a function that writes a textfile '''


def write_file(filename="", text=""):
    ''' read a textfile and print to stdout '''
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
