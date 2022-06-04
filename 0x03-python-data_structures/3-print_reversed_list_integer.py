#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    q = my_list[:: -1]
    for i in range(n):
        print("{}" .format(q[i]))
