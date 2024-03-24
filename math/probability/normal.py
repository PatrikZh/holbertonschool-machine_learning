#!/usr/bin/env python3

class Normal:
    def __init__(self, data=None, mean=0, stddev=1.):
        if data is not None:
            if not isinstance(data, list) or len(data) < 2:
                raise ValueError("data must be a list with multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data) / (len(data))) ** 0.5
        else:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = mean
            self.stddev = stddev

    def cdf(self, x):
        """Calculate the CDF for a given x using a simple approximation."""
        z = (x - self.mean) / self.stddev
        t = 1 / (1 + 0.2316419 * abs(z))
        cdf_approx = 1 - 1/(2.5066282746310002) * (t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429))))) * (2.718281828459045 ** (-z**2 / 2))
        if z < 0:
            return 1 - cdf_approx
        return cdf_approx



