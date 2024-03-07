#!/usr/bin/env python3
"""
function def add_arrays(arr1, arr2):
that adds two arrays element-wise
"""


def add_arrays(arr1, arr2):
    """
   code below
    """
    added_arrays = []
    if len(arr1) != len(arr2):
        return None
    for i, j in zip(arr1, arr2):
        added_arrays.append(i + j)
    return added_arrays
