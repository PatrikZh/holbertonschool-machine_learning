#!/usr/bin/env python3
""" Write a function that calculates the shape of a matrix """


def matrix_shape(matrix):
    """ returns the shape a multi dimensional matrix"""
    matrix_shape = []
    while type(matrix) is list:
        matrix_shape.append(len(matrix))
        matrix = matrix[0]

    return matrix_shape
