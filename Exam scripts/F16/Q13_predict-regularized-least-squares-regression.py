import numpy as np # type: ignore

# Define the weight vectors as numpy arrays
w_a = np.array([0.0538, 0.0558, 0.1861, -0.0596])
w_b = np.array([0.0089, 0.0931, 0.1093, 0.0417])
w_c = np.array([0.2811, 0.0445, 0.3379, -0.4626])
w_d = np.array([0.0167, 0.0698, 0.1354, 0.0403])

# Compute the norms of each weight vector
norms = {
    'w_a': np.linalg.norm(w_a),
    'w_b': np.linalg.norm(w_b),
    'w_c': np.linalg.norm(w_c),
    'w_d': np.linalg.norm(w_d)
}

# Print the norms for inspection
for key, value in norms.items():
    print(f"Norm of {key}: {value}")

# Sort the dictionary by norms (values), get a list of keys based on sorted norms
sorted_weights_by_norm = sorted(norms, key=norms.get, reverse=True)  # largest norm first if reverse is True

# Map sorted weights to their corresponding lambda values (sorted by lambda: 1, 10, 100, 1000)
lambda_mapping = {10: sorted_weights_by_norm[1], 100: sorted_weights_by_norm[2], 1000: sorted_weights_by_norm[3], 1: sorted_weights_by_norm[0]}

# Output the corresponding weight for lambda = 10 
#TODO: Rememebr to up lambda_mapping value based on what lambda is 
print(f"The weight vector corresponding to lambda = 10 is: {lambda_mapping[10]}")
