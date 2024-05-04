import numpy as np

# Data from Table 7 #TODO: Update based on the given dataset
x7 = np.array([-1.76, -0.0, 0.06, 0.08, 0.65, 1.3])
yr = np.array([12, 6, 8, 10, 4, 2])

# Initial Variance
initial_variance = np.var(yr, ddof=0)

# Splitting based on x7 > -0.88
#TODO: Since the task says based on the first split, the script might not work for second
#TODO: Update both right and left on the account of the value of first split 
left_split = yr[x7 <= 0.365]
right_split = yr[x7 > 0.365]

# Variance of the left and right subsets
variance_left = np.var(left_split, ddof=0)
variance_right = np.var(right_split, ddof=0)

# Weighted variance after the split
weighted_variance = (len(left_split) * variance_left + len(right_split) * variance_right) / len(yr)

# Purity gain (Δ)
purity_gain = initial_variance - weighted_variance

print(f"Initial Variance: {initial_variance}")
print(f"Variance Left: {variance_left}")
print(f"Variance Right: {variance_right}")
print(f"Weighted Variance: {weighted_variance}")
print(f"Purity Gain (Δ): {purity_gain}")
