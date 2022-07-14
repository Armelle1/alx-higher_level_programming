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

    def update(self, *args, **kwargs):
        ''' method that updates the square '''
        if not (args is None or len(args) == 0):
            size = len(args)
            if size >= 1:
                self.id = args[0]
            if size >= 2:
                self.size = args[1]
            if size >= 3:
                self.x = args[2]
            if size >= 4:
                self.y = args[3]
        elif kwargs is not None:
            if 'id' in kwargs:
                self.id = kwargs.get('id')
            if 'size' in kwargs:
                self.size = kwargs.get('size')
            if 'x' in kwargs:
                self.x = kwargs.get('x')
            if 'y' in kwargs:
                self.y = kwargs.get('y')

    def to_dictionary(self):
        ''' method that returns the dictionary representation
        of a Square '''
        square_dict = {"id": self.id, "size": self.size}
        square_dict["x"] = self.x
        square_dict["y"] = self.y
        return square_dict

    @property
    def size(self):
        ''' this method gets the size'''
        return self.width

    @size.setter
    def size(self, value):
        ''' this method set the value of size '''
        self.width = value
        self.height = value
