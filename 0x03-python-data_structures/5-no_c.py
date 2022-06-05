#!/usr/bin/python3
def no_c(my_string):
    n = len(my_string)
    p = list(my_string)
    print(p)
    for i in range(n - 3):
        if p[i] == "c" or p[i] == "C":
            del p[i]
            m = "".join(p)
    return (m)
