#!/usr/bin/env python3

class Normal:
    def __init__(self, data=None, mean=0, stddev=1.):
        if data is not None:
            if not isinstance(data, list) or len(data) < 2:
                raise ValueError("data must be a list with multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5
        else:
            self.mean = mean
            self.stddev = stddev
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")

    def cdf(self, x):
        """Approximate the CDF for a given x using a simple polynomial approximation."""
        z = (x - self.mean) / self.stddev
        t = 1.0 / (1.0 + 0.2316419 * z)
        coeffs = [0.319381530, -0.356563782, 1.781477937, -1.821255978, 1.330274429]
        cdf_approx = 1 - (1 / (2 * 3.141592653589793) ** 0.5) * \
                     (t * (coeffs[0] + t * (coeffs[1] + t * (coeffs[2] + t * (coeffs[3] + t * coeffs[4]))))) * \
                     (2.718281828459045 ** (-z ** 2 / 2))
        if z < 0:
            return 1 - cdf_approx
        return cdf_approx


