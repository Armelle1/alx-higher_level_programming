#!/usr/bin/python3
''' this method defines a rectangle'''


class Rectangle:

    '''this class defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''this methode retrieve the width of rectangles'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' this methode set the value of width '''
        if not type(value) is int:
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' this methode gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' this methode set the value of height'''
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')
        self.__height = value
