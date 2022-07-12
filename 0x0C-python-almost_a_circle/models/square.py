#!/usr/bin/python3
''' this method defines a square'''
from models.rectangle import Rectangle


class Square (Rectangle):
    ''' this class defines a square '''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' update str  method '''
        a_str = "[Square] (" + str(self.id) + ") "
        b_str = str(self.x) + "/" + str(self.y) + " - " + str(self.width)
        return a_str + b_str

    def update(self, *args):
        ''' method that updates the rectangle '''
        size = len(args)
        if size >= 1:
            self.id = args[0]
        if size >= 2:
            self.width = args[1]
        if size >= 3:
            self.height = args[2]
        if size >= 4:
            self.x = args[3]
        if size >= 5:
            self.y = args[4]

    @property
    def size(self):
        ''' this method gets the size'''
        return self.width

    @size.setter
    def size(self, value):
        ''' this method set the value of size '''
        self.width = value
        self.height = value
