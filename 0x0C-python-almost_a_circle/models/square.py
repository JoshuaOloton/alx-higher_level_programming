#!/usr/bin/python3
''' square class module '''


from .rectangle import Rectangle


class Square(Rectangle):
    ''' square subclass of imported Base Class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor function '''
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) '\
            f'{self.x}/{self.y} - {self.__size}'
