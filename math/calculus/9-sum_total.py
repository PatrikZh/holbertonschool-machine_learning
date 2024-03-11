#!/usr/bin/env python3
"""
function def summation_i_squared(n):
that calculates sum_{i=1}^{n} i^2
"""


def summation_i_squared(n):
    """
    code below
    """
    if isinstance(n, int) and n > 0:
        return int(n * (n + 1) * (2 * n + 1) / 6)
    else:
        return None
