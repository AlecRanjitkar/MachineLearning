import numpy as np # type: ignore
from sklearn.metrics import roc_curve, auc # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Defining the features based on your description
features = np.array([
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # O1
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # O2
    [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],  # O3
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],  # O4
    [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # O5
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # O6
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],  # O7
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],  # O8
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1],  # O9
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0]   # O10
])

# TODO: Baseret på column (række) i dette tilfælle er x5L række 9
x5L = features[:, 8]

# True labels (1 = safe, 0 = unsafe)
y_true = np.array([1, 0, 1, 1, 1, 0, 0, 0, 0, 1])

# Calculate the ROC curve and AUC
fpr, tpr, _ = roc_curve(y_true, x5L)
roc_auc = auc(fpr, tpr)

# Plotting the ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic for Airline Safety')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
