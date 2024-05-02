import numpy as np

def calculate_classification_error(class_counts):
    # Calculate the classification error for a node
    total = sum(class_counts)
    return 1 - max(class_counts) / total if total > 0 else 0

def calculate_purity_gain(I0, split, n):
    # Calculate purity gain for a given split
    weighted_error = sum((sum(counts) / n) * calculate_classification_error(counts)
                         for counts in split)
    return I0 - weighted_error

# Total number of observations
n = 108 + 112 + 56 + 58 + 75 + 116

# Initial impurity (classification error) for the root node
initial_counts = [108 + 58, 112 + 75, 56 + 116]  # Total counts for each class
I0 = calculate_classification_error(initial_counts)

# Define the splits as lists of class counts for each split
split1 = [(108, 112, 56), (58, 75, 116)]

# Calculate purity gains for each split
purity_gain = calculate_purity_gain(I0, split1, n)

print("Purity gain for the split based on x9:", purity_gain)
