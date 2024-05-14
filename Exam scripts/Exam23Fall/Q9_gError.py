import numpy as np # type: ignore

# Data for outer fold i=1
inner_folds_i1 = {
    "Model 1": [0.12, 0.21, 0.22, 0.23, 0.15],
    "Model 2": [0.30, 0.11, 0.15, 0.30, 0.28],
    "Model 3": [0.21, 0.14, 0.26, 0.17, 0.26]
}
test_errors_i1 = {
    "Model 1": 0.24,
    "Model 2": 0.17,
    "Model 3": 0.22
}

# Data for outer fold i=2
inner_folds_i2 = {
    "Model 1": [0.28, 0.18, 0.19, 0.27, 0.12],
    "Model 2": [0.16, 0.20, 0.27, 0.30, 0.25],
    "Model 3": [0.13, 0.16, 0.21, 0.17, 0.13]
}
test_errors_i2 = {
    "Model 1": 0.19,
    "Model 2": 0.16,
    "Model 3": 0.25
}

# Calculate average validation error for each model in each outer fold
def average_validation_error(inner_folds):
    return {model: np.mean(errors) for model, errors in inner_folds.items()}

avg_val_error_i1 = average_validation_error(inner_folds_i1)
avg_val_error_i2 = average_validation_error(inner_folds_i2)

# Identify the best model in each outer fold
best_model_i1 = min(avg_val_error_i1, key=avg_val_error_i1.get)
best_model_i2 = min(avg_val_error_i2, key=avg_val_error_i2.get)

# Retrieve the test errors for the best models
test_error_best_model_i1 = test_errors_i1[best_model_i1]
test_error_best_model_i2 = test_errors_i2[best_model_i2]

# Calculate the generalization error
generalization_error = np.mean([test_error_best_model_i1, test_error_best_model_i2])

# Output the result
print(f"Generalization Error (E_gen): {generalization_error:.3f}")

