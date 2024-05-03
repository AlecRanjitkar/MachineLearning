# Given probabilities
prior_y1 = 0.316
prior_y2 = 0.356
prior_y3 = 0.328

cond_y1 = 0.25
cond_y2 = 0.2
cond_y3 = 0.35

# Calculate joint probabilities
joint_y1 = cond_y1 * prior_y1
joint_y2 = cond_y2 * prior_y2
joint_y3 = cond_y3 * prior_y3

# Total probability of x2 = 1, x10 = 0
total_probability = joint_y1 + joint_y2 + joint_y3

# Posterior probability for y = 1
posterior_y1 = joint_y1 / total_probability

print(f"Probability p(y = 1 | x2 = 1, x10 = 0) = {posterior_y1:.3f}")
