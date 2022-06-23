#!/usr/bin/python3

""" defines a class Square """


class Square:
    """ class defining a square """
    def __init__(self, size, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def poistion(self, position):
        if type(position) == tuple and len(position) == 2:
            for i in range(2):
                if type(position[i]) != int or postion[i] <= 0:
                    break
            self.__position = position
            return
        raise TypeError('position must be a tuple of 2 positive integers')

    def area(self, value):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(self.__size * '#', end='')
            print()
