#!/usr/bin/python3
def no_c(my_string):
    p = list(my_string)
    i = 0
    for x in p:
        if x == "c" or x == "C":
            p.pop(i)
        i = i + 1
    m = "".join(p)
    return (m)
