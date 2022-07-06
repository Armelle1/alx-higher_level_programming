#!/usr/bin/python3
''' this method'''


def write_file(filename="", text=""):
    ''' this module '''
    with open(filename, 'w+', encoding="utf-8") as f:
        f.write(text)
