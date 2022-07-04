#!/usr/bin/python3
''' this module'''


def inherits_from(obj, a_class):
    ''' this methode'''
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
