def calculate_gini(classes):
    """
    Calculate Gini impurity for a given distribution of classes.
    
    Parameters:
    - classes (list): List of counts of each class in the subset.
    
    Returns:
    - float: Gini impurity value.
    """
    total = sum(classes)
    if total == 0:  # Avoid division by zero
        return 0
    sum_of_squares = sum((count / total) ** 2 for count in classes)
    return 1 - sum_of_squares

def calculate_purity_gain(total_classes, *subsets):
    """
    Calculate the purity gain from a split using Gini impurity.
    
    Parameters:
    - total_classes (list): List of counts of each class before the split.
    - subsets (list of lists): Variable number of lists, each representing class counts in a subset after the split.
    
    Returns:
    - float: Purity gain from the split.
    """
    total_count = sum(total_classes)
    initial_gini = calculate_gini(total_classes)
    weighted_gini = 0
    
    for subset in subsets:
        subset_count = sum(subset)
        weighted_gini += (subset_count / total_count) * calculate_gini(subset)
    
    return initial_gini - weighted_gini

# Example dataset
total_classes = [70,70,70]  # Total distribution of Class A and Class B before split
subset1 = [24,70,0]  # Distribution in subset 1 after split
subset2 = [46,0,70]  # Distribution in subset 2 after split

# Calculate purity gain
purity_gain = calculate_purity_gain(total_classes, subset1, subset2)
print(f"Purity Gain: {purity_gain}")

# TODO: To calculate another split, change `total_classes`, `subset1`, and `subset2` with the new class distributions.
# TODO: If there is a split into more than two subsets, add more subsets as arguments to `calculate_purity_gain`.
# Example for three subsets: purity_gain = calculate_purity_gain(total_classes, subset1, subset2, subset3)
