def calculate_classification_error(classes):
    """
 # TODO: To apply this script to another data set or different split, change the values in `total_classes`, `subset1`, and `subset2`.
# TODO: If the split results in more than two subsets, add more subsets as arguments in the function call.
    Calculate classification error impurity for a given distribution of classes.
    
    Parameters:
    - classes (list): List of counts of each class in the subset.
    
    Returns:
    - float: Classification error impurity value.
    """
    if not classes or sum(classes) == 0:
        return 0
    max_probability = max(classes) / sum(classes)
    return 1 - max_probability

def calculate_purity_gain_classification_error(total_classes, *subsets):
    """
    Calculate the purity gain from a split using classification error impurity.
    
    Parameters:
    - total_classes (list): List of counts of each class before the split.
    - subsets (list of lists): Variable number of lists, each representing class counts in a subset after the split.
    
    Returns:
    - float: Purity gain from the split.
    """
    total_count = sum(total_classes)
    initial_impurity = calculate_classification_error(total_classes)
    weighted_impurity = 0
    
    for subset in subsets:
        subset_count = sum(subset)
        subset_impurity = calculate_classification_error(subset)
        weighted_impurity += (subset_count / total_count) * subset_impurity
    
    return initial_impurity - weighted_impurity

# Example usage
total_classes = [70, 70, 70]  # Total distribution of Kama, Rosa, Canadian
subset1 = [24, 70, 0]  # Distribution in subset 1 after split
subset2 = [46, 0, 70]  # Distribution in subset 2 after split

# Calculate purity gain
purity_gain = calculate_purity_gain_classification_error(total_classes, subset1, subset2)
print(f"Purity Gain: {purity_gain:.4f}")


