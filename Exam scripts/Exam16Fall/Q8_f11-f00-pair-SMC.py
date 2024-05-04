import numpy as np # type: ignore

#TODO: Assuming these cluster assignments from the dendrogram
clusters = {
    'cluster1': [7, 8, 9, 3],  # Including O3 in cluster 1 erroneously with Canadians
    'cluster2': [1, 2],
    'cluster3': [4, 5, 6]
}

# True class labels as per your description
#TODO: look what class they are defined as:
class_labels = {
    1: 'Kama', 2: 'Kama', 3: 'Kama',   # Observations for Kama
    4: 'Rosa', 5: 'Rosa', 6: 'Rosa',   # Observations for Rosa
    7: 'Canadian', 8: 'Canadian', 9: 'Canadian'  # Observations for Canadian
}

# Function to calculate f00 and f11
def calculate_f00_f11(clusters, labels):
    f00, f11 = 0, 0
    all_observations = list(labels.keys())
    K = len(all_observations) * (len(all_observations) - 1) // 2
    for i in range(len(all_observations)):
        for j in range(i + 1, len(all_observations)):
            same_cluster = any(all_observations[i] in clusters[cluster] and all_observations[j] in clusters[cluster] for cluster in clusters)
            same_class = labels[all_observations[i]] == labels[all_observations[j]]
            if same_cluster and same_class:
                f11 += 1
            if not same_cluster and not same_class:
                f00 += 1
    return f00, f11, K

# Calculate f00, f11, and K
f00, f11, K = calculate_f00_f11(clusters, class_labels)

# Calculate SMC
SMC = (f00 + f11) / K
print(f"SMC: {SMC}")
print(f"Total pairs (K): {K}, f00: {f00}, f11: {f11}")
