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
        self.__size = size

    @property
    def size(self):
        '''
        method to retrieve size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
        setter method to set size of square
        '''
        if not type(value) is int:
            raise TypeError('size must be an integer')
        if (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''
        public instance method that returns the current square area
        '''
        c = (self.__size) * (self.__size)
        return c

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''
        size = self.__size
        if size == 0:
            print()
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print()
