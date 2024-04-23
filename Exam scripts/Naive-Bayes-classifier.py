from fractions import Fraction

def calculate_naive_bayes(table, f1, f2, f3):
    # Count the number of instances for each class y=0 and y=1
    count_y0 = sum(1 for row in table if row[-1] == 0)
    count_y1 = sum(1 for row in table if row[-1] == 1)

    # Calculate prior probabilities
    prior_y0 = count_y0 / len(table)
    prior_y1 = count_y1 / len(table)

    # Calculate likelihoods for each feature given the class
    likelihood_f1_y0 = sum(1 for row in table if row[0] == f1 and row[-1] == 0) / count_y0
    likelihood_f2_y0 = sum(1 for row in table if row[1] == f2 and row[-1] == 0) / count_y0
    likelihood_f3_y0 = sum(1 for row in table if row[2] == f3 and row[-1] == 0) / count_y0

    likelihood_f1_y1 = sum(1 for row in table if row[0] == f1 and row[-1] == 1) / count_y1
    likelihood_f2_y1 = sum(1 for row in table if row[1] == f2 and row[-1] == 1) / count_y1
    likelihood_f3_y1 = sum(1 for row in table if row[2] == f3 and row[-1] == 1) / count_y1

    # Calculate the unnormalized posteriors for y=0 and y=1
    unnormalized_posterior_y0 = likelihood_f1_y0 * likelihood_f2_y0 * likelihood_f3_y0 * prior_y0
    unnormalized_posterior_y1 = likelihood_f1_y1 * likelihood_f2_y1 * likelihood_f3_y1 * prior_y1

    # Normalize the posteriors so that they sum to 1
    sum_posteriors = unnormalized_posterior_y0 + unnormalized_posterior_y1
    if sum_posteriors == 0:
        return None  # To avoid division by zero if no evidence supports either class
    posterior_y1 = unnormalized_posterior_y1 / sum_posteriors

    return posterior_y1

# The data from Table 4 converted into a list of lists
# The last element in each sub-list is the class label y, derived from the color coding in the image
table_4_data = [
    [0, 1, 1, 0, 1, 0],  # o1
    [0, 0, 1, 0, 0, 0],  # o2
    [1, 0, 0, 0, 1, 0],  # o3
    [1, 0, 0, 1, 1, 0],  # o4
    [1, 0, 0, 1, 0, 0],  # o5
    [1, 1, 0, 1, 1, 0],  # o6
    [1, 0, 1, 1, 0, 1],  # o7
    [1, 0, 1, 1, 1, 1],  # o8
    [0, 1, 1, 1, 1, 1],  # o9
    [1, 0, 1, 0, 0, 1],  # o10
    [0, 1, 1, 0, 0, 1]   # o11
]

# Example observation from the question
f1_observation = 0
f2_observation = 1
f3_observation = 1

# Calculate the probability
probability = calculate_naive_bayes(table_4_data, f1_observation, f2_observation, f3_observation)

# Calculate the fraction
fraction = Fraction(probability).limit_denominator()

# Print the probability and the fraction
print("Probability:", probability)
print("Fraction:", fraction)
