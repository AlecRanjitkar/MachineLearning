def calculate_jaccard_similarity():
    non_zero_x1 = 1
    non_zero_x2 = 1498
    
    # Best case: x1's non-zero element is one of x2's non-zero elements
    intersection_best = 1
    union_best = non_zero_x2  # Since x2 already covers almost all, x1 adds no new non-zero elements
    
    # Worst case: x1's non-zero element is not one of x2's non-zero elements
    intersection_worst = 0
    union_worst = non_zero_x2 + non_zero_x1  # x1 adds one more non-zero element to the union
    
    jaccard_best = intersection_best / union_best
    jaccard_worst = intersection_worst / union_worst
    
    return jaccard_best, jaccard_worst

best, worst = calculate_jaccard_similarity()
print(f"Jaccard Similarity Range: [{worst:.5f}, {best:.5f}]")

