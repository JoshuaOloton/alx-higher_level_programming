#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
       pass
    def sorted_insert(self, value):
        
