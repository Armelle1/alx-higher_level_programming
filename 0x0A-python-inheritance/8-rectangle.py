#!/usr/bin/python3
''' this module geometry module '''


class BaseGeometry:
    ''' this class '''
    def area(self):
        ''' this methode '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' this methode validates value'''
        if not (type(value) == int):
            raise TypeError(str(name) + ' must be an integer')
        if value <= 0:
            raise ValueError(str(name) + ' must be greater than 0')


class Rectangle(BaseGeometry):
    ''' this class'''
    def __init__(self, width, height):
        ''' this methode'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
