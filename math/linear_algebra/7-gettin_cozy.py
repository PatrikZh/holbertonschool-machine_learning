#!/usr/bin/env python3
"""
function def cat_matrices2D(mat1, mat2, axis=0):
that concatenates two matrices along a specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    code below
    """
    concat_2d_mat = []
    if axis == 0 and len(mat1[0]) == len(mat2[0]):
        concat_2d_mat = mat1 + mat2
    elif axis == 1 and len(mat1) == len(mat2):
        concat_2d_mat = [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
    return concat_2d_mat
