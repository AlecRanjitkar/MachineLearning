import numpy as np

def relu(x):
    """ReLU activation function."""
    return np.maximum(0, x)

def neural_network(x1, x2):
    """Calculates the output of the neural network for given inputs x1 and x2."""
    # Weights from input to hidden layer
    #TODO: Update based on what the task gives you
    w13, w14, w15 = 0.5, 0.5, -0.5
    w23, w24, w25 = 0.5, -0.5, 0.25
    w36, w46, w56 = 0.25, -0.25, 0.25

    # Inputs to the hidden layer neurons
    n3 = x1 * w13 + x2 * w23
    n4 = x1 * w14 + x2 * w24
    n5 = x1 * w15 + x2 * w25

    # Activations of hidden layer neurons
    a3 = relu(n3)
    a4 = relu(n4)
    a5 = relu(n5)

    # Input to the output layer neuron
    n6 = a3 * w36 + a4 * w46 + a5 * w56

    # Output of the network
    output = relu(n6)
    return output

# Example usage with x1 = 1 and x2 = 1
#TODO Update output based on what x1 & x2 is
output = neural_network(1, 1)
print("Output of the neural network:", output)
