#!/usr/bin/python3

""" defines a class Square """


class Square:
    """ class defining a square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
