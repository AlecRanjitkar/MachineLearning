import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# Data points
#TODO: Update observations for X koordinate and Y koordinate based on the task 
X = np.array([[-7], [0], [-4], [5], [27]])
y = np.array([8, 4, 21, 23, 20])

# Create and fit the KNN regressor
#TODO: Update the k value and look to see which matches 
k = 2  # assumed based on observation of changes
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X, y)

# Plotting
X_test = np.linspace(-20, 40, 400).reshape(-1, 1)
y_pred = knn.predict(X_test)

plt.scatter(X, y, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.xlabel('$x_1$')
plt.ylabel('$y$')
plt.title(f'KNN Regression with k={k}')
plt.grid(True)
plt.show()
