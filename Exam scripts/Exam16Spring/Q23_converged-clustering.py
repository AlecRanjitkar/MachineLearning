from sklearn.cluster import KMeans # type: ignore
import numpy as np # type: ignore
#Exam 16 spring question 23, however checkout Exam 18 spring question 25 which uses Init


#TODO: if the assignment tell you to use Init like this below add: 
"initialize the clusters at the locations of the first three observations"
"add init=initial_centers into kmeans"

initial_centers = np.array([[1.0], [1.2], [1.5]])


# The data from the dataset given
#TODO: Update based on the dataset given
data = np.array([[1], [3], [4], [6], [7], [8], [13], [15], [16], [17]])

# Perform K-means clustering with K=4 since the options suggest a division into 4 clusters
#TODO: Update n_clusters based on how many clusters and add init if the tasks says so
"init=initial_centers"

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
