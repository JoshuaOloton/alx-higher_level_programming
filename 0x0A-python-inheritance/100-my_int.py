#!/usr/bin/python3

""" defines a class MyInt that inherits from int """


class MyInt(int):
    """ inherits from builtin list class """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
