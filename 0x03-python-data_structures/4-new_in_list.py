#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    p = tuple(my_list)
    m = list(p)
    if idx < 0:
        return my_list
    if idx > n - 1:
        return my_list
    if idx > 0:
        m[idx] = element
    return m
