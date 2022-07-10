#!/usr/bin/python3

'''  defines function that divides all elements of a matrix. '''


def matrix_divided(matrix, div):
    ''' divides all elements of a matrix. '''
    if not type(div) == int and not type(div) == float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for i in range(1, len(matrix)):
        if len(matrix[i - 1]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
    for row in matrix:
        if False in [isinstance(i, int) or isinstance(i, float) for i in row]:
            raise TypeError('matrix must be a matrix (list of lists\
of integers/floats')
    new_matrix = matrix[:]
    return list(map(lambda x: list(map(lambda y: div/y, x)), new_matrix))
