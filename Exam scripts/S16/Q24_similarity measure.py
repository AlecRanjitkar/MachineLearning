import numpy as np # type: ignore

def similarity_measure(x, y):
    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)
    dot_xy = np.dot(x, y)

    ##Have to update the return 
    return np.sqrt((norm_x**2 * norm_y**2 - dot_xy**2) / (norm_x**2 * norm_y**2))

# Define vectors x and y
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Calculate similarity measure for x and y
original_similarity = similarity_measure(x, y)
print(f"Original similarity: {original_similarity}")

# Scale x and y
alpha = 2
scaled_x = alpha * x
scaled_y = alpha * y
scaled_similarity = similarity_measure(scaled_x, scaled_y)
print(f"Scaled similarity: {scaled_similarity}")

# Translate x and y
beta = np.array([1, 1, 1])
translated_x = x + beta
translated_y = y + beta
translated_similarity = similarity_measure(translated_x, translated_y)
print(f"Translated similarity: {translated_similarity}")
