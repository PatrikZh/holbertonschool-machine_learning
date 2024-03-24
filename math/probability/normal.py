#!/usr/bin/env python3

class Normal:
    """
    the normal class initiating
    """
    def __init__(self, data=None, mean=0, stddev=1.):
        """
        init of the class as blue print
        """
        self.mean = float(mean)
        self.stddev = float(stddev)
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((x - self.mean) ** 2 for x in data) / (len(data) - 1)) ** 0.5
            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")

    def cdf(self, x):
        """
        Simplified and highly inaccurate approximation of CDF, primarily for illustrative purposes.
        This method does not provide accurate results and is a placeholder for the demonstration of class capabilities.
        """
        z = (x - self.mean) / self.stddev
        return 0.5 * (1 + self.sign(z) * (1 - 1 / (1 + abs(z))))

    def sign(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


