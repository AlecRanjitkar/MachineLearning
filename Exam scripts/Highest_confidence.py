from fractions import Fraction
#Examset 16 spring, task 12

def calculate_rule_confidence(table, rule_antecedent, rule_consequent):
    """
    Calculate the confidence of a rule in the format antecedent -> consequent.

    :param table: List of transactions, where each transaction is represented by a list of item flags (0 or 1)
    :param rule_antecedent: Tuple representing the antecedent of the rule (e.g., ('f1', 'f5'))
    :param rule_consequent: Tuple representing the consequent of the rule (e.g., ('f4',))
    :return: Confidence of the rule
    """
    antecedent_count = 0
    both_count = 0
    
    # Convert feature names to indices
    antecedent_indices = [int(item[1])-1 for item in rule_antecedent]
    consequent_indices = [int(item[1])-1 for item in rule_consequent]
    
    # Count the occurrences of the antecedent and both antecedent and consequent
    for transaction in table:
        if all(transaction[index] for index in antecedent_indices):
            antecedent_count += 1
            if all(transaction[index] for index in consequent_indices):
                both_count += 1
    
    # Calculate confidence
    confidence = both_count / antecedent_count if antecedent_count else 0
    return confidence

# Define the transactions data based on the binary matrix given earlier
table_4_data = [
    [0, 1, 1, 0, 1],  # o1
    [0, 0, 1, 0, 0],  # o2
    [1, 0, 0, 0, 1],  # o3
    [1, 0, 0, 1, 1],  # o4
    [1, 0, 0, 1, 0],  # o5
    [1, 1, 0, 1, 1],  # o6
    [1, 0, 1, 1, 0],  # o7
    [1, 0, 1, 1, 1],  # o8
    [0, 1, 1, 1, 1],  # o9
    [1, 0, 1, 0, 0],  # o10
    [0, 1, 1, 0, 0]   # o11
]
# Rules to calculate confidence for
rules = [
    (('f3', 'f4'), ('f5',)),
    (('f1', 'f5'), ('f4',)),
    (('f1', 'f4'), ('f5',)),
    (('f2', 'f4'), ('f1',)),
]

# Calculate confidence for each rule
rule_confidences = {}
for rule in rules:
    rule_confidence = calculate_rule_confidence(table_4_data, *rule)
    rule_confidences[rule] = rule_confidence

# Find the rule with the highest confidence
max_confidence_rule = max(rule_confidences, key=rule_confidences.get)
max_confidence = rule_confidences[max_confidence_rule]

# Find the rule with the lowest confidence
min_confidence_rule = min(rule_confidences, key=rule_confidences.get)
min_confidence = rule_confidences[min_confidence_rule]


# Print out the rule and its confidence as a fraction
max_confidence_fraction = Fraction(max_confidence).limit_denominator()
print(f"Rule with the highest confidence: {max_confidence_rule}")
print(f"Confidence: {max_confidence} or as a fraction: {max_confidence_fraction}")

min_confidence_fraction = Fraction(min_confidence).limit_denominator()
print(f"Rule with the lowest confidence: {min_confidence_rule}")
print(f"Confidence: {min_confidence} or as a fraction: {min_confidence_fraction}")
