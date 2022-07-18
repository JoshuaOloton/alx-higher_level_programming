#!/usr/bin/python3
''' square class module '''


from .rectangle import Rectangle


class Square(Rectangle):
    ''' square subclass of imported Base Class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor function '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size getter '''
        return self.width

    @size.setter
    def size(self, size):
        ''' size setter '''
        self.width = size
        self.height = size

    def __str__(self):
        ''' str function '''
        return f'[{self.__class__.__name__}] ({self.id}) '\
            f'{self.x}/{self.y} - {self.width}'
