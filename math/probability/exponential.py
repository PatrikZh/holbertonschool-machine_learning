#!/usr/bin/env python3
"""
Exponential distribution class evolved with each senquence of code
"""

class Exponential:
    """
    the exponential class
    """
    def __init__(self, data=None, lambtha=1.):
        """
        init of the class as blue print
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            else:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 1:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """
        the pdf function
        """
        e = 2.7182818285
        if x < 0:
            return 0
        else:
            return self.lambtha * e ** (-self.lambtha * x)

    def cdf(self, x):
        """
        the cdf function
        """
        if x < 0:
            return 0
        e = 2.7182818285
        floated = 1 - e ** (-self.lambtha * x)
        if floated == 0:
            return 0.0
        return floated
