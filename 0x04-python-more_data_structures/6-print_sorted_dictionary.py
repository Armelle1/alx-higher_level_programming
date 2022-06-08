#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    p = a_dictionary.keys()
    q = sorted(p)
    for i in q:
        s = print(i, ":", a_dictionary[i])
    return s
