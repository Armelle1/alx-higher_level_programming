#!/usr/bin/python3
def search_replace(my_list, search, replace):
    q = tuple(my_list)
    p = list(q)
    n = len(p)
    for i in range(n):
        if p[i] == search:
            p[i] = replace
    return p
