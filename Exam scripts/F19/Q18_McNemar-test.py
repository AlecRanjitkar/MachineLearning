# Define the values (The values for n12, n21,n is found in table)
n12 = 124  # M1 is correct and M2 is incorrect
n21 = 100  # M2 is correct and M1 is incorrect
N = 981    # Total number of observations

# Compute the estimated difference in accuracy
theta_hat = (n12 - n21) / N

# Print the result
print(f"The estimated difference in accuracy (θ̂) is: {theta_hat:.2f}")
