#!/usr/bin/env python3
"""
function def poly_derivative(poly):
that calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    code below
    """
    if not isinstance(poly, list) or len(poly) < 1:
        return None
    for i in range(len(poly)):
        if not isinstance(poly[i], (int, float)):
            return None
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(poly[i] * i)
    if not derivative:
        derivative = [0]
    return derivative
