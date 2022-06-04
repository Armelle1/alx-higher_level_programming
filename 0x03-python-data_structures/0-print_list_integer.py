#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    p = all ([isinstance (item, int,) for item in my_list])
    if p == True:
        for i in range(n):
            print("{}" .format(my_list[i]))
