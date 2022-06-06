#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # for i in matrix:
    #    m = ' '.join(map(str, i))
    for row in matrix:
        size = len(row)
        for i in range(size):
            if i < size - 1:
                print("{:d} " .format(row[i]), end=" ")
            else:
                print("{:d}" .format(row[i]))
