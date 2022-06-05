#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    liste = []
    for i in range(n):
        p = my_list[i] % 2
        if p == 0:
            liste.append(True)
        else:
            liste.append(False)
    return liste
