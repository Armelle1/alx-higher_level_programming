#!/usr/bin/python3
'''
Square Module
This module prints a square
'''


def print_square(size):
    '''
    this function prints a square with the character #
    '''
    if not type(size) == int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
