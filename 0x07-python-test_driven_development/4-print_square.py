#!/usr/bin/python3

''' defines a function that prints a square with the character # '''


def print_square(size):
    if not type(size) == int:
        raise TypeError('size must be an integer')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size, end='')
        print()
