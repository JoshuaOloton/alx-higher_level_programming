#!/usr/bin/python3
''' Rectangle module '''


from .base import Base


class Rectangle(Base):
    ''' rectangle subclass of imported Base Class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor function '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width getter '''
        return self.__width

    @width.setter
    def width(self, width):
        ''' width setter '''
        if not type(width) == int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        ''' height getter '''
        return self.__height

    @height.setter
    def height(self, height):
        ''' height setter '''
        if not type(height) == int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        ''' x getter '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' x setter '''
        if not type(x) == int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        ''' y getter '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' y setter '''
        if not type(y) == int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        ''' returns area value of instance '''
        return self.width * self.height

    def display(self):
        ''' prints rectangle instance '''
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width, end='')
            print()

    def update(self, *args, **kwargs):
        ''' updates class attributes '''
        arg_list = [self.id, self.width, self.height, self.x, self.y]
        pos = 0
        for arg in args:
            if arg:
                if pos == 0:
                    self.id = arg
                    pos += 1
                elif pos == 1:
                    self.width = arg
                    pos += 1
                elif pos == 2:
                    self.height = arg
                    pos += 1
                elif pos == 3:
                    self.x = arg
                    pos += 1
                elif pos == 4:
                    self.y = arg
                    pos += 1

    def __str__(self):
        ''' str function '''
        return f'[{self.__class__.__name__}] ({self.id}) ' \
            f'{self.x}/{self.y} - {self.width}/{self.height}'
