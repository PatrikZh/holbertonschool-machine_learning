#!/usr/bin/env python3
"""
function def add_matrices2D(mat1, mat2):
that adds two matrices element-wise
"""


def add_matrices2D(arr1, arr2):
    """
    code below
    """
    if len(arr1) != len(arr2) or len(arr1[0]) != len(arr2[0]):
        return None
    added_arrays = [[i + j for i, j in zip(row1, row2)]
                    for row1, row2 in zip(arr1, arr2)]
    return added_arrays
    