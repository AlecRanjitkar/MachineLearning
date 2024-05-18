import itertools


def find_extended_itemsets_with_support(table, num_items, min_support_ratio):
    """
    Find all itemsets (single items, pairs, triples, etc.) that occur with at least a given support ratio.

    :param table: List of transactions, where each transaction is represented by a list of item flags (0 or 1)
    :param num_items: The number of items (up to 10 in this case)
    :param min_support_ratio: The minimum support ratio
    :return: A list of itemsets that meet the minimum support ratio
    """
    itemsets = []
    num_transactions = len(table)
    min_support_count = min_support_ratio * num_transactions

    # Generate all possible itemsets of size 1 to min(num_items, 10)
    for size in range(1, min(num_items, 10) + 1):
        for itemset in itertools.combinations(range(num_items), size):
            support_count = sum(all(transaction[i] for i in itemset) for transaction in table)
            if support_count >= min_support_count:
                itemsets.append({f'x{i+1}' for i in itemset})

    return itemsets

# Sample table of transactions
table_data = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Transaction 1
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Transaction 2
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 0],  # Transaction 3
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],  # Transaction 4
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 1],  # Transaction 5
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Transaction 6
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # Transaction 7
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],  # Transaction 8
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],  # Transaction 9
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],  # Transaction 10
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Transaction 11
    [1, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # Transaction 12
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],  # Transaction 13
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0]   # Transaction 14
]

# Set the number of items and the minimum support ratio
num_items = 10  # Number of items
min_support_ratio = 0.40  # Minimum support ratio

# Calculate extended itemsets with support greater than the given ratio
extended_itemsets_with_support = find_extended_itemsets_with_support(table_data, num_items, min_support_ratio)
print("Extended itemsets with sufficient support:", extended_itemsets_with_support)
