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
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
