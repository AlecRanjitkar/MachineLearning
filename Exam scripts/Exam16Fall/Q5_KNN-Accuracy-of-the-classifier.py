import numpy as np # type: ignore

# Define the confusion matrix
confusion_matrix = np.array([
    [31, 1, 3],  # Predictions for Kama
    [5, 30, 0],  # Predictions for Rosa
    [6, 0, 29]   # Predictions for Canadian
])

# Calculate the number of correct predictions (sum of diagonal elements)
correct_predictions = np.trace(confusion_matrix)

# Calculate the total number of predictions (sum of all elements)
total_predictions = np.sum(confusion_matrix)

# Calculate accuracy
accuracy = correct_predictions / total_predictions

# Print the accuracy
print(f"The accuracy of the classifier is: {accuracy:.4f}")
