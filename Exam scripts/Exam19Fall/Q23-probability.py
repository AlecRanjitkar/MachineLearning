import numpy as np # type: ignore

# Probabilities of pollution levels
#Number of observations
N = 981
#TODO: Update based on the task
p_y1 = 391 / N
p_y2 = 241 / N
p_y3 = 349 / N

# Probabilities of high O3 given pollution levels
#TODO: Update here based on the task
p_x1_given_y1 = 64 / 391
p_x1_given_y2 = 66 / 241
p_x1_given_y3 = 206 / 349

# Convert to probabilities of low O3 given pollution levels
p_x0_given_y1 = 1 - p_x1_given_y1
p_x0_given_y2 = 1 - p_x1_given_y2
p_x0_given_y3 = 1 - p_x1_given_y3

# Bayes' Theorem to find p(y = 2 | x = 0)
numerator = p_x0_given_y1 * p_y1
denominator = (p_x0_given_y1 * p_y1) + (p_x0_given_y2 * p_y2) + (p_x0_given_y3 * p_y3)
light_p_y2_given_x0 = numerator / denominator

numerator2 = p_x0_given_y2 * p_y2
denominator2 = (p_x0_given_y1 * p_y1) + (p_x0_given_y2 * p_y2) + (p_x0_given_y3 * p_y3)
medium_p_y2_given_x0 = numerator2 / denominator2


numerator3 = p_x0_given_y3 * p_y3
denominator3 = (p_x0_given_y1 * p_y1) + (p_x0_given_y2 * p_y2) + (p_x0_given_y3 * p_y3)
high_p_y2_given_x0 = numerator3 / denominator3

print("Probability of light pollution level given low O3 concentration: ", light_p_y2_given_x0)
print("Probability of medium pollution level given low O3 concentration: ",medium_p_y2_given_x0)
print("Probability of high pollution level given low O3 concentration: ",high_p_y2_given_x0)
