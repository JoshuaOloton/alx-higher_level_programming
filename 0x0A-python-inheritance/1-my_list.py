#!/usr/bin/python3

""" defines a class MyList that inherits from list """


class MyList(list):
    def print_sorted(self):
        self.__new_list = self[:]
        self.__new_list.sort()
        print(self.__new_list)
