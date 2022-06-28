#!/usr/bin/python
'''
Module Texit 
The module Text indentation
'''


def text_indentation(text):
    '''
    this function prints a text with specific indentation
    '''
    if not type(text) is str:
        raise TypeError('text must be a string')
    for car in text:
        print(car, end="")
        if (car == '.' or car == '?' or car == ':'):
            print("\n\n", end="")
