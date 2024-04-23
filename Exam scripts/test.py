def find_itemsets_with_support(table, num_items, min_support_ratio):
    """
    Find all itemsets (single items and pairs) that occur with at least a given support ratio.

    :param table: List of transactions, where each transaction is represented by a list of item flags (0 or 1)
    :param num_items: The number of items M
    :param min_support_ratio: The minimum support ratio
    :return: A list of itemsets that meet the minimum support ratio
    """

    
    itemsets = []
    num_transactions = len(table)
    min_support_count = min_support_ratio * num_transactions
    
    # Check support for individual items
    for item in range(num_items):
        support_count = sum(transaction[item] for transaction in table)
        if support_count >= min_support_count:
            itemsets.append({f'f{item+1}'})
    
    # Check support for pairs of items
    for item1 in range(num_items):
        for item2 in range(item1+1, num_items):
            support_count = sum(transaction[item1] and transaction[item2] for transaction in table)
            if support_count >= min_support_count:
                itemsets.append({f'f{item1+1}', f'f{item2+1}'})
    
    return itemsets

# M = 5 items, with support greater than 0.32
M = 10
support_ratio = 0.55

table_4_data = [
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # o2
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o3
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],  # o4
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # o5
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 0],  # o6
    [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],  # o7
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 1],  # o8
    [0, 0, 0, 0, 1, 1, 1, 0, 1, 1],  # o9
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0]   # o10
]

# Calculate itemsets with support greater than 0.32, including item pairs
itemsets_with_support = find_itemsets_with_support(table_4_data, M, support_ratio)
print(itemsets_with_support)