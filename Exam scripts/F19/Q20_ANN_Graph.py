import numpy as np

def sigmoid(x):
    """Sigmoid activation function that maps any real value into the range 0 to 1"""
    return 1 / (1 + np.exp(-x))

# Define the weights (TODO: Update these weights according to the new neural network's architecture and trained values)
w1_1 = np.array([-0.5, -0.1])
w2_1 = np.array([0.9, 2.0])
w0_2 = 1.4
w1_2 = -1.0
w2_2 = 0.4

# Input values (TODO: Update or provide new input values according to your dataset)
x1 = 1  # Often 1 is used for a bias term, if not relevant, set as needed
x2 = -2  # The variable condition you are testing

# Input to the first layer neurons (TODO: Adjust the number of neurons or structure if the network is different)
z1 = np.dot(np.array([x1, x2]), w1_1)
z2 = np.dot(np.array([x1, x2]), w2_1)

# Activation from the first layer
a1 = sigmoid(z1)
a2 = sigmoid(z2)

# Input to the second layer neuron (TODO: Adjust if your network's second layer is structured differently)
z3 = w0_2 + w1_2 * a1 + w2_2 * a2

# Output from the second layer (final output) (TODO: Add more layers if needed or adjust according to your network)
output = sigmoid(z3)

print("The neural network output is:", output)
