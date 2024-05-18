
table_4_data = [
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # o2
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o3
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],  # o4
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o5
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],  # o6
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],  # o7
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],  # o8
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],  # o9
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]  # o10
]
from fractions import Fraction

def feature_set_present(transaction, feature_set):
    """Check if all features in feature_set are present in the transaction."""
    return all(transaction[f-1] == 1 for f in feature_set)

def calculate_confidence(data, antecedent, consequent):
    antecedent_count = 0
    both_count = 0
    
    for transaction in data:
        if feature_set_present(transaction, antecedent):
            antecedent_count += 1
            if feature_set_present(transaction, consequent):
                both_count += 1
    
    if antecedent_count == 0:
        return 0  # To avoid division by zero if the antecedent never occurs
    return both_count / antecedent_count

# Define the antecedent and consequent feature indices
# Note: corrected indices as per your previous comment to include f2 in antecedent (if intended)

#TODO: do not follow start from 0, we always start from 1
antecedent = [1, 3, 8, 9, 2]  # Assuming f2 was intentionally added
consequent = [2, 6, 7]

# Calculate the confidence
confidence = calculate_confidence(table_4_data, antecedent, consequent)
fraction_confidence = Fraction(confidence).limit_denominator()

# Print the confidence
print("Confidence of the rule is:", confidence)
print("Fraction:", fraction_confidence)
