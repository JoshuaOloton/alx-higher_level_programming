#!/usr/bin/python3

''' defines Base Class '''


class Base:
    ''' package Base Class '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
