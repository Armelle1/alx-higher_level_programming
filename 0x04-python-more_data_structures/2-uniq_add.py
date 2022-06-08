#!/usr/bin/python3
def uniq_add(my_list=[]):
    q = list(set(my_list))
    n = len(q)
    p = 0
    for i in range(n):
        p = p + q[i]
    return p
