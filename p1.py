'''
Initial test code to demonstrate the properties and actions of a single neuron.

Each neuron takes in inputs from a previous neuron, finds the dot product of the inputs and a set of tunable weights,
then adds a set bias.

'''

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias

print(output)

'''
Simplify above code using the dot product in numpy.

'''
import numpy as np 

output = np.dot(weights, inputs) + bias
print(output)