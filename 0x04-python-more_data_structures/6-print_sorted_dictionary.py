#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # p = a_dictionary.keys
    for i in sorted(a_dictionary):
        print(i, a_dictionary[i])
