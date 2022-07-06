#!/usr/bin/python3
''' this module '''


def append_write(filename="", text=""):
    ''' this module '''
    with open(filename, "a+") as f:
        f.write(text)
