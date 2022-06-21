#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        # self._size = size
        try:
            if not type(size) is int:
                raise TypeError('size must be an integer')
            if (size <= 0):
                raise ValueError('size must be >= 0')
            self._size = size
        except Exception as e:
            print(e)
