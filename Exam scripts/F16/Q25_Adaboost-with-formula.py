import numpy as np # type: ignore

def adaboost_weight_update(N, misclassified_count, initial_weight):
    # Calculate the error rate (epsilon)
    epsilon_t = misclassified_count / N

    # Calculate alpha_t using the formula: 0.5 * log((1 - epsilon) / epsilon)
    alpha_t = 0.5 * np.log((1 - epsilon_t) / epsilon_t)

    # Calculate the new weights for misclassified observations
    new_weight_misclassified = initial_weight * np.exp(alpha_t)

    # Calculate the new weights for correctly classified observations
    new_weight_correct = initial_weight * np.exp(-alpha_t)

    # Calculate normalization factor Z_t to ensure weights sum to 1
    Z_t = (N - misclassified_count) * new_weight_correct + misclassified_count * new_weight_misclassified

    # Normalize the weights
    normalized_weight_misclassified = new_weight_misclassified / Z_t
    normalized_weight_correct = new_weight_correct / Z_t

    return normalized_weight_misclassified, normalized_weight_correct, Z_t

# Parameters
N = 25  # Total number of observations
misclassified_count = 5  # Number of misclassified observations
initial_weight = 1 / N  # Initial uniform weight

# Get the updated weights for misclassified observations
updated_weight_misclassified, updated_weight_correct, normalization_factor = adaboost_weight_update(N, misclassified_count, initial_weight)
print(f"Normalization factor: {normalization_factor:.3f}")
print(f"The updated weights for classifed observations based on Adaboost is: {updated_weight_correct:.3f}")
print(f"The updated weights for misclassifed observations based on Adaboost is: {updated_weight_misclassified:.3f}")
