import numpy as np

conversions = np.array([50, 65, 80, 45, 70, 90, 55, 85, 60, 75])
print("Original:", conversions)

median = np.median(conversions)
variance = np.var(conversions)
std = np.std(conversions)

print("Median:", median)
print("Variance:", variance)
print("Std:", std)

uniform = np.random.uniform(0, 100, 10)
ints = np.random.randint(0, 100, 10)
floats = np.random.random(10) * 100
normal = np.random.normal(50, 15, 10)

all_data = np.concatenate([conversions, uniform, ints, floats, normal])

mean_val = np.mean(all_data)

print("Mean:", mean_val)

print("Greater than 2000?", mean_val > 2000)