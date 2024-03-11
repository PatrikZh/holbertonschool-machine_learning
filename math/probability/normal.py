#!/usr/bin/env python3
import math
"""
Normal distribution class evolved with each senquence of code
"""


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
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((ent - self.mean) ** 2 for ent in data)
                           / len(data)) ** 0.5
    def z_score(self, x):
        """
        z score function
        """
        return float((x - self.mean) / self.stddev)

    def x_value(self, z):
        """
        x value function
        """
        return float(self.mean + z * self.stddev)
    
    def pdf(self, x):
        """
        Calculate the probability density function for a given x.
        """
        coeff = 1 / (self.stddev * math.sqrt(2 * math.pi))
        exponent = math.exp(-(x - self.mean) ** 2 / (2 * self.stddev ** 2))
        return coeff * exponent
