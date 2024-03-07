def __init__(self, data=None, lambtha=1.):
    """ """
    self.lambtha = float(lambtha)
    if self.lambtha <= 0:
        raise ValueError("lambtha must be a postitive value")
    if data is not None:
        if type(data) is not list:
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lambtha = float(sum(data)) / len(data)

def pmf(self, k):
    """ Calculates the value of the PMF for a given number of successes """
    if type(k) is not int:
        k = int(k)
    if k < 0:
        return 0
    e = 2.7182818285
    lambtha = self.lambtha
    factorial = 1
    for i in range(k):
        factorial *= (k + 1)
        pmf = (e** - lambtha) * (lambtha ** k ) / factorial
        return pmf

def cdf(self, k):
    """ """
    if type(k) is not int:
        k = int(k)
    if k < 0:
        return 0 
    cdf = 0
    for i in range(k+1):
        