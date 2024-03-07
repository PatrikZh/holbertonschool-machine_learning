#!/usr/bin/env python3
"""
function def np_elementwise(mat1, mat2):
that performs element-wise addition, subtraction, multiplication, 
and division
"""


def np_elementwise(mat1, mat2):
    """ code below """
    result = []
    result.append(mat1 + mat2)
    result.append(mat1 - mat2)
    result.append(mat1 * mat2)
    result.append(mat1 / mat2)
    return result