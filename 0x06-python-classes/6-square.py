#!/usr/bin/python3
''' The module Square that defines a square'''


class Square:
    '''
    The class Square defines a square
     '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Constructs all the necessary attributes for the square object
        '''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''
         method to retrieve the position of square
        '''
        return self.__position

    @position.setter
    def position(self, value):
        '''
        setter method to set the position of square
        '''
        x = value[0]
        y = value[1]
        if not(type(value) is tuple and type(x) is int and x >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not (type(y) is int and y >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
        position = self.__position
        if size == 0:
            print()
        else:
            for i in range(size):
                if position[0] > 0:
                    for k in range(position[0]):
                        print(" ", end="")
                for j in range(size):
                    print("#", end="")
                print()
