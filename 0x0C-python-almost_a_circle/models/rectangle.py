#!/usr/bin/python3
''' this method defines a rectangle'''
from models.base import Base

class Rectangle(Base):
    ''' this class defines a rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not type(width) is int:
             raise TypeError('width must be an integer')
        if (width <= 0):
            raise ValueError('width must be > 0')

        if not type(height) is int:
            raise TypeError('height must be an integer')
        if (height <= 0):
            raise ValueError('height must be > 0')

        if not type(x) is int:
            raise TypeError('x must be an integer')
        if (x < 0):
            raise ValueError('x must be >= 0')

        if not type(y) is int:
            raise TypeError('y must be an integer')
        if (y < 0):
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''this method retrieve the width of rectangles'''
        return self.__width

    @width.setter
    def width(self, width):
        ''' this method set the value of width '''
        if not type(width) is int:
            raise TypeError('width must be an integer')
        if (width <= 0):
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        ''' this method gets the height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' this method set the value of height'''
        if not type(value) is int:
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' the getter of x '''
        return self.__x

    @property
    def y(self):
        ''' the getter of y '''
        return self.__y

    @x.setter
    def x(self, x):
        ''' the setter of x '''
        if not type(x) is int:
            raise TypeError('x must be an integer')
        if (x < 0):
            raise ValueError('x must be >= 0')
        self.__x = x

    @y.setter
    def y(self, y):
        ''' the setter of y '''
        if not type(y) is int:
            raise TypeError('y must be an integer')
        if (y < 0):
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):

        ''' return the rectangle area'''
        c = self.__width * self.__height
        return c

    def perimeter(self):
        ''' return the rectangle perimeter '''
        c = (self.__width + self. __height) * 2
        if (self.__width == 0 or self.__height == 0):
            c = 0
        return c

    def display(self):
        ''' This public method prints the Rectangle '''
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
