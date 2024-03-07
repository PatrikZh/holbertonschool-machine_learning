#!/usr/bin/env python3
"""
function def matrix_transpose(matrix): 
that returns the transpose of a 2D matrix, matrix
"""


def matrix_transpose(matrix):
    """
   code below
    """
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0]) if matrix else 0

    transposed_matrix = [[matrix[j][i] for j in range(matrix_rows)]
                         for i in range(matrix_cols)]
    return transposed_matrix