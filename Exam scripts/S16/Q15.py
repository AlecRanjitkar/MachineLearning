def calculate_humidity_probability(conditional_probs):
    """
    Calculate the probability that a room is humid given that it is occupied.

    Args:
    conditional_probs (dict): A dictionary with the given conditional probabilities.

    Returns:
    float: The calculated probability.
    """
    # P(g2 = 1 | y = 1) = P(g1 = 0, g2 = 1 | y = 1) + P(g1 = 1, g2 = 1 | y = 1)
    probability_humid_occupied = (conditional_probs.get('P(g1=0, g2=1 | y=1)') +
                                  conditional_probs.get('P(g1=1, g2=1 | y=1)'))
    return probability_humid_occupied

# Given conditional probabilities
given_probs = {
    'P(g1=0, g2=1 | y=1)': 0.03,
    'P(g1=1, g2=1 | y=1)': 0.50
}

# Calculate the probability
humidity_probability = calculate_humidity_probability(given_probs)
print(humidity_probability)