#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    first_key = list(a_dictionary)[0]
    i = -1000
    for p in a_dictionary:
        if a_dictionary[p] > i:
            i = a_dictionary[p]
            key = p
    return key
