#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list)
    print (all ([isinstance (item, int,) for item in my_list]))
    for i in range(n):
        m_string = "{}"
        print(m_string.format(my_list[i]))
