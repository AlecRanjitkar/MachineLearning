def calculate_classification_error(class_counts):  
    # Calculate the classification error for a node  
    total = sum(class_counts)  
    return 1 - max(class_counts) / total if total > 0 else 0  
  
def calculate_purity_gain(I0, split, n):  
    # Calculate purity gain for a given split  
    weighted_error = sum((count / n) * calculate_classification_error((observed, count - observed))  
                         for observed, count in split)  
    return I0 - weighted_error  
  
# Initial impurity (classification error) for the root node  
I0 = 1 - 1/2  # For a perfectly balanced binary classification  
  
# Number of observations TODO: Update n based on task
n = 200  
  
# Define the splits (occupied, total) from your teacher's solution  
#TODO, Update based on task, left is occupied right is total
splits_info = {  
    'Split 1': [(45, 46), (66, 113), (33, 41)],  # Split 1: (occupied, total)  
    'Split 2': [(20, 76), (47, 63), (33, 41)],   # Split 2  
    'Split 3': [(0, 25), (23, 78), (77, 97)]     # Split 3  
}  
  
# Calculate purity gains for each split and find the best split  
purity_gains = {split_label: calculate_purity_gain(I0, split, n) for split_label, split in splits_info.items()}  
best_split = max(purity_gains, key=purity_gains.get)  
best_purity_gain = purity_gains[best_split]  
  
# Output the results and the chosen split  
for split_label, purity_gain in purity_gains.items():  
    print(f"Purity gain for {split_label}: {purity_gain:.3f}")  
    if split_label == best_split:  
        print(f"{split_label} is chosen by Hunt's algorithm with a purity gain of {purity_gain:.3f}\n")  
  
# Print comparison between splits  
for split_label, purity_gain in purity_gains.items():  
    if split_label != best_split:  
        print(f"{best_split} is selected over {split_label} because {best_purity_gain:.4f} > {purity_gain:.4f}")