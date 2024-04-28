import numpy as np  
  
# V matrix from the second image  
V = np.array([
    [-0.5939, 0.2906, -0.3413, 0.0621, 0.6652],
    [0.6521, 0.0759, 0.0004, 0.3813, -0.6508],
    [0.2028, -0.5105, -0.7036, 0.4508, 0.0010],
    [-0.3696, -0.5414, -0.1781, -0.7244, -0.1173],
    [-0.2102, -0.5967, 0.5973, 0.3503, 0.3467]
])
  
# Extracting the second principal component (v2)  
v2 = V[:, 1]  # This is the second column of V  
  
# Computing -3v2 - 1v2  
result_vector = 1 * v2
  
# Display the result  
print(result_vector)


#result
#[ 2.  -2.4  1.6  0.4 -1.6]
# 2 = x1, -2.4 = x2, etc...
#If negative coefficent negative impact, otherwise positive impact

# We see the temperature goes up, the humidity drops and the light goes up, therefore option A is correct.
