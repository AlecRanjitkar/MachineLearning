#TODO: L is pruning level so update L based on level
def calculate_models(K1, K2, L=3):
    """ Calculate the total number of models trained for given K1, K2. """
    return K1 * (K2 * L + 1)

#TODO update max_modul based on the task
def evaluate_all_strategies(options, max_models=100):
    """ Evaluate each option and print total models trained, checking against the budget. """
    results = []
    for K1, K2 in options:
        total_models = calculate_models(K1, K2)
        within_budget = total_models <= max_models
        results.append((K1, K2, total_models, within_budget))
    return results

# Options provided as (K1, K2) tuples
#TODO Update options based on the given values.
options = [(6, 5), (3, 11), (14, 2), (4, 9)]

# Evaluate all strategies
results = evaluate_all_strategies(options)

# Print all strategies and their evaluation
for result in results:
    print(f"K1 = {result[0]}, K2 = {result[1]}, Total Models = {result[2]}, Within Budget = {'Yes' if result[3] else 'No'}")




#TODO: If We have to find for other than K1 and k2 use this, remember to update max_models and num_pruning based on the task


# def find_valid_cv_strategies(max_models, num_pruning_levels):
#     valid_strategies = []
#     for K1 in range(1, max_models + 1):
#         for K2 in range(1, max_models + 1):
#             total_models = K1 * K2 * num_pruning_levels
#             if total_models <= max_models:
#                 valid_strategies.append((K1, K2, total_models))
#     return valid_strategies

# # Number of pruning levels considered in inner CV
# num_pruning_levels = 3

# # Maximum number of models that can be trained
# max_models = 100

# # Get valid strategies
# valid_strategies = find_valid_cv_strategies(max_models, num_pruning_levels)

# # Print the strategies
# for strategy in valid_strategies:
#     print("K1 = {}, K2 = {}, Total Models Trained = {}".format(strategy[0], strategy[1], strategy[2]))
