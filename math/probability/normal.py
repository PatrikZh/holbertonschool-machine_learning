#!/usr/bin/env python3
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

    def pdf(self, x):
        """
        pdf function
        """
        p = 3.1415926536
        e = 2.7182818285
        return ((1 / (self.stddev * ((2 * p) ** 0.5))) *
                (e ** (-0.5 * ((x - self.mean) / self.stddev) ** 2))

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
