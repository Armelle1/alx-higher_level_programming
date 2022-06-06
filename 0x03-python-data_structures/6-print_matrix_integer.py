#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # for i in matrix:
    #    m = ' '.join(map(str, i))
    for row in matrix:
        for item in row:
            print("{:d} " .format(item), end=" ")
        print()
