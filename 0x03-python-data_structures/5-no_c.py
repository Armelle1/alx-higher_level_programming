#!/usr/bin/python3
def no_c(my_string):
    n = len(my_string)
    i = 0
    p = list(my_string)
    for i in range(n):
        if p[i] == "c" or p[i] == "C":
            del p[i]
            m = "".join(p)
            return (m)
