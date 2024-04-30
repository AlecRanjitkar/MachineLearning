import numpy as np # type: ignore
# Exam set 16 question 21

# Define the softmax function
def softmax(scores):
    exp_scores = np.exp(scores)
    return exp_scores / np.sum(exp_scores)

# Data point
x = np.array([0, 1])

# Weight vectors for each option
weights = {
    'A': [np.array([-1, -1]), np.array([1, 1]), np.array([1, -1])],
    'B': [np.array([1, -1]), np.array([-1, -1]), np.array([1, 1])],
    'C': [np.array([1, 1]), np.array([-1, -1]), np.array([1, -1])],
    'D': [np.array([-1, -1]), np.array([1, 1]), np.array([-1, 1])]
}

# Calculate and print the softmax probabilities for each option
for option, ws in weights.items():
    scores = np.array([np.dot(w.T, x) for w in ws])
    probabilities = softmax(scores)
    print(f"Option {option}:")
    print(f"Scores: {scores}")
    print(f"Softmax Probabilities: {probabilities}")
    print(f"Class with the highest probability: {np.argmax(probabilities) + 1}")
    print()  # Newline for better readability between options

