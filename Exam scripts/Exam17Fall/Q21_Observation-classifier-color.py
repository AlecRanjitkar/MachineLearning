from scipy.spatial.distance import jaccard # type: ignore

# Hypothetical binary data for O1 to O10
#TODO: update based on dataset
data = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0]
]

# Compute Jaccard distance (1 - Jaccard similarity index) for O10 against others
#TODO: Change data[9] based on which observation it has to be for
o10 = data[9]

jaccard_scores = [('O' + str(i+1), 1 - jaccard(o10, data[i])) for i in range(9)]

# Sort based on highest similarity (lowest distance, since we used 1 - similarity)
sorted_scores = sorted(jaccard_scores, key=lambda x: x[1], reverse=True)

# Get top 3 similar observations
top_three = sorted_scores[:3]

# Display results
print("We can see the 3 nearest neighbor classifier to classify observation is")
print(top_three)
