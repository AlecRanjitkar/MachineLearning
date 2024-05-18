import numpy as np # type: ignore

# Heights of the players
#TODO: Update based on the given observation
heights = np.array([5.7, 6.0, 6.2, 6.3, 6.4, 6.6, 6.7, 6.9, 7.0, 7.4])

# Function to calculate Euclidean distance
def euclidean_distance(x, y):
    return np.abs(x - y)

# Function to calculate the density for an observation based on its K nearest neighbors
def calculate_density(data, index, K):
    distances = np.array([euclidean_distance(data[index], data[j]) for j in range(len(data)) if j != index])
    nearest_distances = np.partition(distances, K)[:K]
    density = 1 / np.mean(nearest_distances)  # Density as reciprocal of the average distance
    print(f"Densities for index {index} with distances {nearest_distances}: {density}")
    return density

# Calculate Average Relative Density for observation O10
def calculate_ard(data, index, K):
    distances = np.array([euclidean_distance(data[index], data[j]) for j in range(len(data)) if j != index])
    nearest_indices = np.argsort(distances)[:K]
    densities = np.array([calculate_density(data, i, K) for i in range(len(data))])
    density_o10 = calculate_density(data, index, K)
    ard = density_o10 / np.mean(densities[nearest_indices])
    print(f"Nearest indices for O10: {nearest_indices}")
    print(f"ARD calculation: {density_o10} / Mean densities of neighbors {np.mean(densities[nearest_indices])}")
    return ard

# Calculate ARD for O10, which is at index 9 in the array
#TODO: update based on what your K is and the index value (9) 
# Based on where in the observation O value is located
K = 3
ard_o10 = calculate_ard(heights, 9, K)

print(f"Average Relative Density for O10 with {K} nearest neighbors: {ard_o10:.4f}")
