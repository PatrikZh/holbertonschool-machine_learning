#!/usr/bin/env python3
"""
Normal file
"""


class Normal:
    """
    the exponential class
    """
    def __init__(self, data=None, mean=0, stddev=1.):
        if data is not None:
            if not isinstance(data, list) or len(data) < 2:
                raise ValueError("data must be a list with multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data)
                / len(data)) ** 0.5
        else:
            self.mean = mean
            self.stddev = stddev
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

    def cdf(self, x):
        """
        Approximate the CDF for a given x
        using a simple polynomial approximation.
        """
        mean = self.mean
        stddev = self.stddev
        pi = 3.1415926536
        value = (x - mean) / (stddev * (2 ** (1 / 2)))
        erf = value - ((value ** 3) / 3) + ((value ** 5) / 10)
        erf = erf - ((value ** 7) / 42) + ((value ** 9) / 216)
        erf *= (2 / (pi ** (1 / 2)))
        cdf = (1 / 2) * (1 + erf)
        return cdf
