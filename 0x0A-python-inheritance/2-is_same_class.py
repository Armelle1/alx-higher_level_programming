#!/usr/bin/python3
''' this module returns the instance of an object'''


def is_same_class(obj, a_class):
    ''' this class return True for the sepcified class'''
    if type(obj) is a_class:
        return True
    else:
        return False
