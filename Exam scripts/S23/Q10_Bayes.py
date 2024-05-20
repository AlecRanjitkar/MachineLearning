# Total observations
N = 8760

# Observations with low, medium, and high demand
LD = 3285
MD = 2190
HD = 3285

# Observations with low humidity given low, medium, and high demand
LH_LD = 1327
LH_MD = 1718
LH_HD = 2344

# Probabilities of low, medium, and high demand
P_LD = LD / N
P_MD = MD / N
P_HD = HD / N

# Probabilities of low humidity given low, medium, and high demand
P_LH_LD = LH_LD / LD
P_LH_MD = LH_MD / MD
P_LH_HD = LH_HD / HD

# Probabilities of high humidity given low, medium, and high demand
P_HH_LD = 1 - P_LH_LD
P_HH_MD = 1 - P_LH_MD
P_HH_HD = 1 - P_LH_HD

# Total probability of high humidity
P_HH = P_HH_LD * P_LD + P_HH_MD * P_MD + P_HH_HD * P_HD

# Probability of high demand given high humidity (using Bayes' theorem)
P_HD_HH = P_HH_HD * P_HD / P_HH

print("The probability of observing high demand given a high value of Humidity is:", P_HD_HH)