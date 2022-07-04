#!/usr/bin/python3

""" defines function that returns True if the object is exactly an instance of the specified class ; otherwise False """


class MyList(list):
    def print_sorted(self):
        self.__new_list = self[:]
        self.__new_list.sort()
        print(self.__new_list)
