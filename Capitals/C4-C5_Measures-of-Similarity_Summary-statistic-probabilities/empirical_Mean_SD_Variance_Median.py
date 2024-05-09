
import statistics

# Given dataset
data = [1, 3, 3, 1, 2, 3, 1]

# Calculate the mean
mean = statistics.mean(data)
print("Empirical Mean:", mean)

# Calculate the standard deviation
std_dev = statistics.stdev(data)
print("Empirical Standard Deviation:", std_dev)

# Calculate the variance
variance = statistics.variance(data)
print("Impirical Variance:", variance)

median = statistics.median(data)
print("Median:", median)


