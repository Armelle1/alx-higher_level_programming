#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    if a_dictionary is None:
        return None
    for p in a_dictionary:
        if a_dictionary[p] > i:
            i = a_dictionary[p]
            key = p
    return key
