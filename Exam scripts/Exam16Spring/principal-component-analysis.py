import numpy as np

#From Examset spring 2016 Question 2:

# Singular values from the S matrix
singular_values = np.array([149, 118, 53, 42, 3])

# Calculate the variance explained by each principal component
variance_explained = (singular_values ** 2) / np.sum(singular_values ** 2)
variance_explained_cumsum = np.cumsum(variance_explained) * 100  # cumulative variance explained in percentage

first_component_variance = variance_explained_cumsum[0]
first_two_components_variance = variance_explained_cumsum[1]
last_two_components_variance = variance_explained_cumsum[-1] - variance_explained_cumsum[-3]
last_three_components_variance = variance_explained_cumsum[-1] - variance_explained_cumsum[-4]
first_three_components_variance = variance_explained_cumsum[2]
first_four_components_variance = variance_explained_cumsum[3]
last_four_components_variance = variance_explained_cumsum[-1] - variance_explained_cumsum[0]

# Printing the results
print("Cumulative Variance Explained by Each Component: ", variance_explained_cumsum)
print("Variance Explained by the First Component: {:.2f}%".format(first_component_variance))
print("Variance Explained by the First Two Components: {:.2f}%".format(first_two_components_variance))
print("Variance Explained by the Last Two Components: {:.2f}%".format(last_two_components_variance))
print("Variance Explained by the Last Three Components: {:.2f}%".format(last_three_components_variance))
print("Variance Explained by the First Three Components: {:.2f}%".format(first_three_components_variance))
print("Variance Explained by the First Four Components: {:.2f}%".format(first_four_components_variance))
print("Variance Explained by the Last Four Components: {:.2f}%".format(last_four_components_variance))