#!/usr/bin/python
'''The module adds 2 integers'''


def add_integer(a, b=98):
    '''
    this function adds 2 integer
    '''
    if not (type(a) is int or type(a) is float):
        raise TypeError('a must be an integer')
    if not (type(b) is int or type(b) is float):
        raise TypeError('b must be an integer')
    c = int(a) + int(b)
    return c
