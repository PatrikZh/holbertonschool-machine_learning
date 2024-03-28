#!/usr/bin/env python3
"""
A class Neuron that defines a single neuron performing binary classification
"""


import numpy as np


class NeuralNetwork:
    """
    A single neuron performing binary classification
    """
    def __init__(self, nx, nodes):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError("nodes must be an integer")
        if nodes < 1:
            raise ValueError("nodes must be a positive integer")

        self.W1 = np.random.randn(nodes, nx)
        self.b1 = np.zeros((nodes, 1))
        self.A1 = 0

        self.W2 = np.random.randn(1, nodes)
        self.b2 = 0
        self.A2 = 0

        @property
        def W1(self):
            """ get method for property W1"""
            return self.__W1

        @property
        def b1(self):
            """ get method for property b1"""
            return self.__b1

        @property
        def A1(self):
            """ get method for property A1"""
            return self.__A1

        @property
        def W2(self):
            """ get method for property W2"""
            return self.__W2

        @property
        def b2(self):
            """ get method for property b2"""
            return self.__b2

        @property
        def A2(self):
            """ get method for property A2"""
            return self.__A2
