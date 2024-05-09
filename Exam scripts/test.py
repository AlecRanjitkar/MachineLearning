import numpy as np

# Define matrices
x1 = np.array([[0.6], [0.2]])  # red plus
x2 = np.array([[0.4], [0.9]])  # black circle
y1 = np.array([[0.5], [0.25]]) # corresponding to x1
y2 = np.array([[0.5], [0.5]])  # corresponding to x2

# One-norm (Manhattan norm)
norm_x1_y1_1 = np.linalg.norm(x1 - y1, 1)
norm_x2_y2_1 = np.linalg.norm(x2 - y2, 1)
print("One-norm of (x1 - y1):", norm_x1_y1_1)
print("One-norm of (x2 - y2):", norm_x2_y2_1)

# Two-norm (Euclidean norm)
norm_x1_y1_2 = np.linalg.norm(x1 - y1)
norm_x2_y2_2 = np.linalg.norm(x2 - y2)
print("Two-norm of (x1 - y1):", norm_x1_y1_2)
print("Two-norm of (x2 - y2):", norm_x2_y2_2)

# Infinity norm (Max norm)
norm_x1_y1_inf = np.linalg.norm(x1 - y1, np.inf)
norm_x2_y2_inf = np.linalg.norm(x2 - y2, np.inf)
print("Infinity norm of (x1 - y1):", norm_x1_y1_inf)
print("Infinity norm of (x2 - y2):", norm_x2_y2_inf)

# Option A calculations (seems to be just a specific norm print, but without clear specification)
# Option A seems to be using the infinity norm for A, and Euclidean norm for B
A = norm_x1_y1_inf
B = norm_x2_y2_2
print("A:", A)
print("B:", B)

# Book's method with identity matrix (which is a method to calculate Euclidean distance squared)
I = np.eye(len(x2))
B = np.sqrt(np.transpose(x2 - y2) @ I @ (x2 - y2))
print("nB (calculated according to book's method):", B)
