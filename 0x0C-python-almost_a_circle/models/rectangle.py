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
        for yy in range(self.__y):
            print()
        for i in range(self.__height):
            for xx in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        ''' update str  method '''
        a_str = "[Rectangle] (" + str(self.id) + ") "
        b_str = str(self.__x) + "/" + str(self.__y) + " - "
        c_str = str(self.__width) + "/" + str(self.__height)
        return a_str + b_str + c_str

    def update(self, *args, **kwargs):
        ''' method that updates the rectangle '''
        if not (args is None or len(args) == 0):
            size = len(args)
            if size >= 1:
                self.id = args[0]
            if size >= 2:
                self.width = args[1]
            if size >= 3:
                self.height = args[2]
            if size >= 4:
                self.x = args[3]
            if size >= 5:
                self.y = args[4]
        elif kwargs is not None:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'width' in kwargs:
                self.width = kwargs.get('width')
            if 'height' in kwargs:
                self.height = kwargs.get('height')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')
