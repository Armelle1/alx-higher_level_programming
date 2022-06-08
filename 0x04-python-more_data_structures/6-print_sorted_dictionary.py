#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
   # p = a_dictionary.keys()
   # q = sorted(p)
    # for i in q:
       # s = print(i, ":", a_dictionary[i])
    #return s
    p = a_dictionary.items()
    for i in sorted(p):
        print(i[0], ":", i[1])

