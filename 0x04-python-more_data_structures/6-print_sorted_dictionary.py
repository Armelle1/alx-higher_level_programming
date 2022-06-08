#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    p = a_dictionary.keys()
    print(p)
    q = sorted(p)
    for i in q:
        print(i, ":", a_dictionary[i])
