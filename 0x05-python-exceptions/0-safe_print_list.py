#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        p = my_list[0:x]
        for i in p:
            print(i, end='')
            c = c + 1
    except Exception:
        pass
    print()
    return c
