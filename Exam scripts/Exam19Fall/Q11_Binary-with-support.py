from mlxtend.frequent_patterns import apriori
import pandas as pd

# Define the binary table
data = {
    'f1': [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    'f2': [0, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    'f3': [0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    'f4': [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    'f5': [0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
    'f6': [1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    'f7': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'f8': [1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    'f9': [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
    'f10': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'f11': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Todo update min_support
frequent_itemsets = apriori(df, min_support=0.65, use_colnames=True)

# Convert the itemsets to the same format as the multiple-choice options
formatted_itemsets = []
for itemset in frequent_itemsets['itemsets']:
    formatted_itemset = "{" + ", ".join(sorted(itemset)) + "}"
    formatted_itemsets.append(formatted_itemset)

print(formatted_itemsets)
