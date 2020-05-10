'''
Code layers as objects
'''

import numpy as np

np.random.seed(0) # Ensure consistent results

X = [   [1, 2, 3, 2.5],
        [2.0, 5.0, -1.0, 2.0],
        [-1.5, 2.7, 3.3, -0.8]
]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons) #Make weights random and small
        self.biases = np.zeros((1, n_neurons)) #Start bias at 0
    
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 500) #n_neurons can be whatever you want
layer2 = Layer_Dense(500, 2) #input must match n_neurons of previous layer

layer1.forward(X)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)

