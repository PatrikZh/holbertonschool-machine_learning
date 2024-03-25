#!/usr/bin/env python3
"""
A class Neuron that defines a single neuron performing binary classification
"""


import numpy as np


class Neuron:
    """
    A single neuron performing binary classification
    """
    def __init__(self, nx):
        """class constructor"""
        if type(nx) is not int:
            raise TypeError("nx must be integer")
        if nx < 1:
            raise ValueError("ns must be a positive integer")
        self.W = np.random.randn(1, nx)
        self.b = 0
        self.A = 0
