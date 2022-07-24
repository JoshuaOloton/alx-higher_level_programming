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

    def update(self, *args, **kwargs):
        ''' update Square instance '''
        pos = 0
        if args:
            for arg in args:
                if pos == 0:
                    self.id = arg
                if pos == 1:
                    self.size = arg
                if pos == 2:
                    self.x = arg
                if pos == 3:
                    self.y = arg
                pos += 1
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def __str__(self):
        ''' str function '''
        return f'[{self.__class__.__name__}] ({self.id}) '\
            f'{self.x}/{self.y} - {self.width}'
