#!/usr/bin/python3
'''this module'''


class MyList(list):
    ''' this class inherits of my list'''
    def print_sorted(self):
        if not type(self) is None:
            print(sorted(self))
