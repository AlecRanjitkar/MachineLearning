import numpy as np # type: ignore

# Define matrices and vectors
X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y = np.array([2, 3, 5, 4])

# Calculate X^T * X and X^T * y
XTX = np.dot(X.T, X)
XTy = np.dot(X.T, y)

# Calculate the inverse of X^T * X
XTX_inv = np.linalg.inv(XTX)

# Calculate optimal weights
w_star = np.dot(XTX_inv, XTy)

# Calculate predicted y and error
y_pred = np.dot(X, w_star)
errors = y - y_pred
SSE = np.dot(errors.T, errors)

# Output results
print("Optimal weights (w*):", w_star)
print("Sum of Squares Error (SSE):", SSE)
