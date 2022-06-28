#!/usr/bin/python3
'''
Printing module
this module prints first name and last name
'''


def say_my_name(first_name, last_name=""):
    '''
    this function allows to print first name and last name
    '''
    if not type(first_name) == str:
        raise TypeError('first_name must be a string')
    if not type(last_name) == str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}" .format(first_name, last_name))
