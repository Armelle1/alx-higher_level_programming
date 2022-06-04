#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    p = all ([isinstance (item, int,) for item in my_list])
    if (p == True):
         q = my_list[:: -1]
         for i in range(n):
             print("{}" .format(q[i]))
