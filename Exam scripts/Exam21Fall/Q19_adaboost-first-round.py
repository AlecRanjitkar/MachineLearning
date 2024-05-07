from fractions import Fraction
import numpy as np # type: ignore

# Initial values
N = 572  # Number of observations
initial_weight = 1 / N
accuracy = 3 / 4

# Calculate error rate
epsilon = 1 - accuracy

# Calculate alpha
alpha = 0.5 * np.log((1 - epsilon) / epsilon)

# Update weights for a correctly classified instance
updated_weight = initial_weight * np.exp(-alpha)
fraction = Fraction(updated_weight).limit_denominator()
# Print calculations
print("Epsilon (Error rate):", epsilon)
print("Alpha (Learner's weight):", alpha)
print("Updated weight for a correctly classified instance:", updated_weight)

