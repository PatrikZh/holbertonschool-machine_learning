#!/usr/bin/env python3
"""
function def poly_integral(poly, C=0):
that calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    code below
    """
    if not isinstance(poly, list):
        return None
    if not isinstance(C, int):
        return None
    if not poly:
        return None
    integral_result = [coef / (index + 1) for index, coef in enumerate(poly)]
    integral_result.insert(0, C)
    integral_result = [int(coef) if int(coef) == coef
                       else coef for coef in integral_result]
    while integral_result[-1] == 0 and len(integral_result) > 1:
        integral_result.pop()
    return integral_result
