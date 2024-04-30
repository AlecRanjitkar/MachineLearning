import numpy as np  
  
def calculate_density(nearest_distances, K):  
    """  
    Calculate the density for a given observation based on its K-nearest neighbors.  
    Parameters:    - nearest_distances: A list of distances from the observation to its K-nearest neighbors.    - K: The number of nearest neighbors to consider.  
    Returns:    - The density value for the observation.    """    # Ensure the list is sorted and take the K smallest distances  
    if len(nearest_distances) > K:  
        nearest_distances = sorted(nearest_distances)[:K]  
    return 1 / np.mean(nearest_distances)  
  
def calculate_ard(nearest_distances_o, nearest_distances_neighbors, K):  
    """  
    Calculate the average relative density (a.r.d.) for a given observation.  
    Parameters:    - nearest_distances_o: A list of distances from the observation to its K-nearest neighbors.    - nearest_distances_neighbors: A list of lists, each containing distances from each neighbor to its K-nearest neighbors.    - K: The number of nearest neighbors to consider.  
    Returns:    - The average relative density (a.r.d.) for the observation.    """    
    density_o = calculate_density(nearest_distances_o, K)  
    densities_neighbors = [calculate_density(distances, K) for distances in nearest_distances_neighbors]  
    return density_o / np.mean(densities_neighbors)  
  
# Example usage  

# Remember whatever K is, is the amount of neighbours to find. fo remember to add them.
K = 2  
nearest_distances_o9 = [1.95, 0.73]  # Distances to the two nearest neighbors o6 and o8  
nearest_distances_o6 = [1.95, 2.01]  # Distances from o6 to its two nearest neighbors  
nearest_distances_o8 = [0.73, 2.03]  # Distances from o8 to its two nearest neighbors  
  
# Calculate a.r.d. for o9  
ard_o9 = calculate_ard(nearest_distances_o9, [nearest_distances_o6, nearest_distances_o8], K)  
  
# Print the result  
print(f"Average Relative Density (a.r.d.) of o9: {ard_o9:.4f}")
