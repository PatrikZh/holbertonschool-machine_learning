#!/usr/bin/env python3
"""
function def mat_mul(mat1, mat2):
that performs matrix multiplication
"""


def mat_mul(mat1, mat2):
    """ code below"""
    mat_multipla = []
    if len(mat1[0]) != len(mat2):
        return None
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            element = 0
            for k in range(len(mat2)):
                element += mat1[i][k] * mat2[k][j]
            row.append(element)
        mat_multipla.append(row)
    return mat_multipla
