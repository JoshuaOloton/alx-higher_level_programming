#!/usr/bin/python3

''' defines a class Student '''


class Student:
    def __init__(self, first_name, last_name, age):
        ''' class constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' retrieves dictionary representation of instance '''
        new_dict = {}
        if not attrs or len(attrs) == 0:
            return self.__dict__
        for string in attrs:
            if string in self.__dict__.keys():
                new_dict[string] = self.__dict__[string]
        return new_dict
