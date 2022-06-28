#!/usr/bin/python
'''
Matrix module
The module Divide a matrix
'''


def matrix_divided(matrix, div):
    '''
    this function divided all elements of a matrix
    '''
    error = 'matrix must be a matrix (list of lists) of integers/floats'
    error2 = 'Each row of the matrix must have the same size'
    if not (type(div) is int or type(div) is float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not (matrix):
        raise TypeError(error)
    if not type(matrix[0]) is list:
        raise TypeError(error)
    nb_rows = len(matrix)
    nb_columns = len(matrix[0])
    result_matrix = []
    for i in range(nb_rows):
        column = []
        for j in range(nb_columns):
            value = matrix[i][j]
            if len(matrix[i]) != nb_columns:
                raise TypeError(error2)
            if not (type(matrix[i]) is list and type(matrix) is list):
                raise TypeError(error)
            if not (type(value) is int or type(value) is float):
                raise TypeError(error)
            result = value / div
            column.append(round(result, 2))
        result_matrix.append(column)
    return result_matrix
