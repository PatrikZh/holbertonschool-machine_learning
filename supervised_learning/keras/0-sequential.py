#!/usr/bin/env python3
"""
Write a function def build_model(nx, layers, activations, lambtha, keep_prob)
that builds a neural network with the Keras library
"""

import tenserflow.keras as K

def build_model(nx, layers, activations, lambtha, keep_prob):
    """ 
nx is the number of input features to the network
layers is a list containing the number of nodes in each layer of the network
activations is a list containing the activation functions 
used for each layer of the network
lambtha is the L2 regularization parameter
keep_prob is the probability that a node will be kept for dropout
    """
    model = K.Sequential()

    for i in range(len(layers)):
        model.add(K.layers.Dense(layers[i],
                  activation=activations[i],
                  kernel_regularizer=K.regularizers.L2(lambtha),
                  input_dim=nx))
        # apply dropout except on output layer
        if i != len(layers) - 1 and keep_prob is not None:
            model.add(K.layers.Dropout(1-keep_prob))

    return model
