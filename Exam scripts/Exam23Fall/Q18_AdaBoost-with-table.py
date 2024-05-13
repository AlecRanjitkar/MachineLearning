import numpy as np # type: ignore

def update_adaboost_weights(y_true, y_pred, N):
    # Initialize weights equally
    weights = np.full(N, 1 / N)
    
    # Determine which predictions are incorrect
    incorrect = y_true != y_pred
    
    # Calculate the error rate (epsilon)
    epsilon = np.sum(weights[incorrect]) / np.sum(weights)
    
    # Compute the performance of the classifier (alpha)
    alpha = 0.5 * np.log((1 - epsilon) / epsilon)
    
    # Update weights
    # Increase weights for incorrectly classified examples
    weights[incorrect] *= np.exp(alpha)
    # Decrease weights for correctly classified examples
    weights[~incorrect] *= np.exp(-alpha)
    
    # Normalize the weights
    weights /= np.sum(weights)
    
    return weights

# True class labels and predicted outputs
#TODO: Update based on the given table
y_true = np.array([2, 2, 1, 2, 1, 1])
y_pred = np.array([2, 2, 2, 1, 2, 2])

# Number of observations
#TODO: Update based on N
N = 6

# Update weights using AdaBoost
updated_weights = update_adaboost_weights(y_true, y_pred, N)

# Print the updated, normalized weights
print("Updated weights:", np.round(updated_weights, 3))
