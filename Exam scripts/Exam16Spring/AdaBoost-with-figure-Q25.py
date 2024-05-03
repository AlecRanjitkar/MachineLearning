import numpy as np # type: ignore

# Initial weights
N = 6  # Number of observations
initial_weights = np.full(N, 1/N)

# Misclassified observations (assuming 0-indexed positions as in usual Python arrays)
misclassified = [1,5]  # Based on the error analysis from the image

# Error of the classifier
epsilon = sum(initial_weights[misclassified]) / sum(initial_weights)

# Performance of the classifier
alpha = 0.5 * np.log((1 - epsilon) / epsilon)

# Update weights
new_weights = np.array([w * np.exp(-alpha) if i not in misclassified else w * np.exp(alpha)
                        for i, w in enumerate(initial_weights)])

# Normalize weights
new_weights /= np.sum(new_weights)

# Round the weights for easier interpretation
rounded_weights = np.round(new_weights, 3)
print(rounded_weights)
