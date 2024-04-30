#Exam 16 spring question 3

import numpy as np  
  
# V matrix from the second image  
V = np.array([  
    [-0.3, -0.5,  0.7,  0.2,  0.2],  
    [-0.4,  0.6, -0.0,  0.2,  0.7],  
    [-0.4, -0.4, -0.7,  0.4, -0.0],  
    [-0.6, -0.1, -0.1, -0.8,  0.1],  
    [-0.5,  0.4,  0.2,  0.2, -0.7]  
])  
  
# Extracting the second principal component (v2)  
v2 = V[:, 1]  # This is the second column of V  
  
# Computing -3v2 - 1v2  
result_vector = -3 * v2 - 1 * v2  
  
# Display the result  
print(result_vector)


#result
#[ 2.  -2.4  1.6  0.4 -1.6]
# 2 = x1, -2.4 = x2, etc...
#If negative coefficent negative impact, otherwise positive impact

# We see the temperature goes up, the humidity drops and the light goes up, therefore option A is correct.
