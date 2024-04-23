import numpy as np
#Examset 16 spring, task 13
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def simple_matching_coefficient(vec1, vec2):
    return sum(1 for i, j in zip(vec1, vec2) if i == j) / len(vec1)

def jaccard_similarity(vec1, vec2):
    intersection = sum(1 for i, j in zip(vec1, vec2) if i == j and i == 1)
    union = sum(1 for i, j in zip(vec1, vec2) if i == 1 or j == 1)
    return intersection / union

# Observations from Table 4 as 5-dimensional binary vectors
o1 = np.array([0, 1, 1, 0, 1])
o2 = np.array([0, 0, 1, 0, 0])
o3 = np.array([1, 0, 0, 0, 1])

# Calculate similarities and coefficients
cos_o1_o2 = cosine_similarity(o1, o2)
smc_o1_o2 = simple_matching_coefficient(o1, o2)
cos_o1_o3 = cosine_similarity(o1, o3)
j_o1_o3 = jaccard_similarity(o1, o3)

# Print the results
print("Cosine Similarity between o1 and o2:", cos_o1_o2)
print("Cosine Similarity between o1 and o3:", cos_o1_o3)
print("Simple Matching Coefficient between o1 and o2:", smc_o1_o2)
print("Jaccard Similarity between o1 and o3:", j_o1_o3)

# Check the validity of the statements
statement_a = cos_o1_o2 > smc_o1_o2
statement_b = cos_o1_o2 > cos_o1_o3
statement_c = j_o1_o3 > smc_o1_o2
statement_d = j_o1_o3 > cos_o1_o3

print("\nValidity of the statements:")
print("Statement A (COS(o1,o2) > SMC(o1,o2)): ", statement_a)
print("Statement B (COS(o1,o2) > COS(o1,o3)): ", statement_b)
print("Statement C (J(o1,o3) > SMC(o1,o2)): ", statement_c)
print("Statement D (J(o1,o3) > COS(o1,o3)): ", statement_d)
