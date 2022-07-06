#!/usr/bin/python3
''' this method'''


def read_file(filename=""):
    ''' this module '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
