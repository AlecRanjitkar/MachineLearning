import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Class labels (actual outcomes): 0s are negative, 1s are positive 
# TODO update based on the figure look from bottum left to top right, if you dont understand look at the question for this examset.
y_true = [1, 1, 0, 1, 0, 0]  # Actual classes of the points 

# Simulated probability scores of being positive
y_scores = [0.9,0.85, 0.6, 0.4, 0.1, 0.1]  # Assuming decision boundary at around 0.5

# Compute ROC curve
fpr, tpr, thresholds = roc_curve(y_true, y_scores)

# Calculate AUC
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

# Print the AUC in decimal
print("AUC in decimal: ", roc_auc)

# Convert AUC to fraction using np's fraction representation
from fractions import Fraction
fraction_auc = Fraction(roc_auc).limit_denominator()
print("AUC in fraction: ", fraction_auc)
