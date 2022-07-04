#!/usr/bin/python3

""" defines function that returns True if the object is an instance of a
class that inherited (directly or indirectly) from the specified class ;
otherwise False."""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that inherited
from the specified class """
    return isinstance(obj, a_class) and not obj.__class__ == a_class
