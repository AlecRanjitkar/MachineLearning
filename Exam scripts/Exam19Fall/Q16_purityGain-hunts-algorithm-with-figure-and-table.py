import numpy as np # type: ignore

# Data from Table 7
#TODO:
x1 = np.array([-1.76, -0.0, 0.06, 0.08, 0.65, 1.3])
yr = np.array([12, 6, 8, 10, 4, 2])

# Initial Variance
initial_variance = np.var(yr, ddof=0)

# First split based on x1 > 0.365
#TODO: Update based on tree figure 
left_indices = x1 <= 0.365
right_indices = x1 > 0.365
left_split = yr[left_indices]
right_split = yr[right_indices]
right_x1 = x1[right_indices]  # Also split x1 to keep dimensions consistent

# Variance of the left and right subsets after the first split
variance_left = np.var(left_split, ddof=0)
variance_right = np.var(right_split, ddof=0)

# Weighted variance after the first split
weighted_variance_first_split = (len(left_split) * variance_left + len(right_split) * variance_right) / len(yr)

# Purity gain after the first split
purity_gain_first_split = initial_variance - weighted_variance_first_split

# Second split for the right split based on x1 > -0.88

#TODO: Update based on tree figure 
second_left_indices = right_x1 <= (-0.88)
second_right_indices = right_x1 > (-0.88)
left_split_left = right_split[second_left_indices]
left_split_right = right_split[second_right_indices]

# Variance of the left and right subsets after the second split
variance_right_left = np.var(left_split_left, ddof=0)
variance_right_right = np.var(left_split_right, ddof=0)

# Weighted variance after the second split
weighted_variance_second_split = (len(left_split_left) * variance_right_left + len(left_split_right) * variance_right_right) / len(right_split)

# Purity gain after the second split
purity_gain_second_split = variance_right - weighted_variance_second_split

print(f"Initial Variance: {initial_variance:.4f}")
print(f"Variance Left after first split: {variance_left:.4f}")
print(f"Variance Right after first split: {variance_right:.4f}")
print(f"Weighted Variance after first split: {weighted_variance_first_split:.4f}")
print(f"Purity Gain after first split: {purity_gain_first_split:.4f}")
print(f"Variance Left after second split: {variance_right_left:.4f}")
print(f"Variance Right after second split: {variance_right_right:.4f}")
print(f"Weighted Variance after second split: {weighted_variance_second_split:.4f}")
print(f"Purity Gain after second split: {purity_gain_second_split:.4f}")
