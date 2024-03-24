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
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum((ent - self.mean) ** 2 for ent in data) / len(data)) ** 0.5

    def z_score(self, x):
        """
        z score function
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        x value function
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """
        Approximate the probability density function for a given x.
        """
        pi = 3.141592653589793
        e = 2.718281828459045
        coeff = 1 / (self.stddev * (2 * pi) ** 0.5)
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        return coeff * (e ** exponent)
    
    def cdf(self, x):
        """
        A very simple and inaccurate approximation of CDF for educational purposes.
        """
        z = (x - self.mean) / self.stddev
        return 0.5 * (1 + self.sign(z) * (1 - 1 / (1 + abs(z))))

    def sign(self, x):
        """
        Utility function to return the sign of x.
        """
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0

