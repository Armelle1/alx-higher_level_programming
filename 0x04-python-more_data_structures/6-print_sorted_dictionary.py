#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    p = a_dictionary.items()
    for i in sorted(p):
        q = print(i[0], ":", i[1])
    return q
