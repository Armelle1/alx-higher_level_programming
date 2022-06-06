#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)
    if n == 0:
        tuple_a = (0, 0)
    elif n == 1:
        tuple_a = (tuple_a[0], 0)
    if m == 0:
        tuple_b = (0, 0)
    elif m == 1:
        tuple_b = (tuple_b[0], 0)
    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]
    s = (sum1, sum2)
    return (s)
