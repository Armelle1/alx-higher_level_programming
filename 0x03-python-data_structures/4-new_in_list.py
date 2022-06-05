#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    p = tuple(my_list)
    m = list(p)
    if idx < 0:
        return m
    if idx > n - 1:
        return m
    if idx > 0:
        m[idx] = element
    return m
