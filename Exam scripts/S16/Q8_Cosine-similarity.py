import numpy as np   # type: ignore
  
  
def cosine_similarity(norm_o1, norm_o2, euclidean_distance):  
    """  
    Calculate cosine similarity between two observations.  
    Parameters:    - norm_o1: Euclidean norm of the first observation    - norm_o2: Euclidean norm of the second observation    - euclidean_distance: Euclidean distance between the two observations  
    Returns:    - Cosine similarity value    """    # Calculate the squared norms  
    squared_norm_o1 = norm_o1 ** 2  
    squared_norm_o2 = norm_o2 ** 2  
  
    # Calculate the squared Euclidean distance  
    squared_euclidean_distance = euclidean_distance ** 2  
  
    # Calculate the dot product from the norms and Euclidean distance  
    dot_product = (squared_norm_o1 + squared_norm_o2 - squared_euclidean_distance) / 2  
  
    # Calculate the cosine similarity  
    cosine_sim = dot_product / (norm_o1 * norm_o2)  
  
    return cosine_sim  
  
  
# Example usage from task:   #TODO update norm_o2 and 3 bases on the task
norm_o2 = 3.04  
norm_o3 = 1.5  
euclidean_distance_o2_o3 = 4.40 ## From the table  #TODO should look at the distance based on norms 
# Calculate cosine similarity  
cos_sim = cosine_similarity(norm_o2, norm_o3, euclidean_distance_o2_o3)  
  
print(f"The cosine similarity is approximately {cos_sim:.4f}")