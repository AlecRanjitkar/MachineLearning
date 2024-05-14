# Given probabilities and mean
probabilities = [0.5, 0.46, 0.14]
values = [1, 2, 3]
mean = 1.6

# Calculate the variance
variance = sum(p * (k - mean) ** 2 for p, k in zip(probabilities, values))

# Output the result
print(f"Variance: {variance:.3f}")
