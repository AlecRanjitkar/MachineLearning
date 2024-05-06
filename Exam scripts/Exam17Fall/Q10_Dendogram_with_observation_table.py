import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from scipy.cluster.hierarchy import dendrogram, linkage # type: ignore
from scipy.spatial.distance import pdist, squareform # type: ignore

# Array of observations
#TODO: update based on observation
observations = np.array([5.7, 6.0, 6.2, 6.3, 6.4, 6.6, 6.7, 6.9, 7.0, 7.4])

# Calculate the pairwise distances
distance_matrix = pdist(observations.reshape(-1, 1), metric='euclidean')

# Perform hierarchical clustering using complete linkage
linked = linkage(distance_matrix, 'average')

# Plot the dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           labels=range(1, 11),  #TODO:# Update based on ranged
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Dendrogram for Hierarchical Clustering of Observations')
plt.xlabel('Index of Point')
plt.ylabel('Distance')
plt.show()
