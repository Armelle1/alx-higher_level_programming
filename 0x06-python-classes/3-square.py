#!/usr/bin/python3
''' The module Square that defines a square'''


class Square:
    '''
    The class Square defines a square
     '''
    def __init__(self, size=0):
        '''
        Constructs all the necessary attributes for the square object
        '''
        if not type(size) is int:
            raise TypeError('size must be an integer')
        if (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''
        public instance method that returns the current square area
        '''
        c = (self.__size) * (self.__size)
        return c
