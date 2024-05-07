import numpy as np # type: ignore

# TODO: CHOOSE ANY OF THE ACTIVATION FUNCTIONS FROM BELOW AND IF UNSURE WHICH TO CHOOSE, TEST ALL AND SEE WHICH MATCHES

def relu(x):
    """ReLU activation function."""
    return np.maximum(0, x) # Relu will give rectified linear outputs

def sigmoid(x):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def tanh(x):
    """Tanh activation function."""
    return np.tanh(x)

def softmax(x):
    """Softmax activation function."""
    e_x = np.exp(x - np.max(x))  # shift values for numerical stability
    return e_x / e_x.sum(axis=0)  # sum across features if the input is a vector

def linear(x):
    """Linear activation function."""
    return x

def leaky_relu(x, alpha=0.01):
    """Leaky ReLU activation function."""
    return np.where(x > 0, x, x * alpha)

def elu(x, alpha=1.0):
    """ELU activation function."""
    return np.where(x >= 0, x, alpha * (np.exp(x) - 1))



# Inputs
x1 = 6
x2 = 120
x3 = 3.2
x4 = 0
x5 = 4

w1_1 = np.array([-4, 1, 0.01, 1, -1, -1])
w2_1 = np.array([-10, 1, -0.02, 1, 1, 1])

w0_2 = 7
w1_2 = 8
w2_2 = 9
# Calculating the output using the given weights and activation function
output = (w1_2 * tanh( w1_1[0]+ w1_1[1] * x1 + w1_1[2] * x2 + w1_1[3] * x3 + w1_1[4] * x4 + w1_1[5] * x5) +
          w2_2 * tanh(w2_1[0] + w2_1[1] * x1 + w2_1[2] * x2 + w2_1[3] * x3 + w2_1[4] * x4 + w2_1[5] * x5) +
          w0_2)

print("Predicted fuel consumption:", output)
