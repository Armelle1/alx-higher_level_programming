#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    if cond(all([isinstance(item, int,) for item in my_list])) is True:
        for i in range(n):
            print("{}" .format(my_list[i]))
