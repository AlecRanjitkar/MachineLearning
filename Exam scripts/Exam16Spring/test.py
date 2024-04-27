from sklearn.cluster import KMeans
import numpy as np

# The data from Table 7 converted into a numpy array

#TODO: Update based on the dataset given
data = np.array([[1], [3], [4], [6], [7], [8], [13], [15], [16], [17]])

# Perform K-means clustering with K=4 since the options suggest a division into 4 clusters
#TODO: try to update n_clusters to see which matches the
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data)

# Retrieve the cluster centers and the labels
centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Now to find the clustering corresponding to a converged state of the K-means algorithm,
# we will group the data points based on the labels assigned by K-means
clusters = {}
for label, point in zip(labels, data):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(point[0])

# Sort each cluster and sort the list of clusters by their first element for easy comparison with options
sorted_clusters = sorted([sorted(cluster) for cluster in clusters.values()], key=lambda x: x[0])

# Show the sorted clusters
print(sorted_clusters)  
