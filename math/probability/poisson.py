#!/usr/bin/env python3
"""
Poisson distribution evolved with each senquence of code
"""


class Poisson:
    """
    the poisson  class
    """
    def __init__(self, data=None, lambtha=1):
        """
        init of the class as blue print
        """
        self.lambtha = float(lambtha)
        if self.lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        the first parameters
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        lambtha = self.lambtha
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        pmf = ((e ** -lambtha) * lambtha ** k) / factorial
        return pmf

    def cdf(self, k):
        """
        Takes in control the calucations for a given number of success
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf