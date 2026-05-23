import numpy as np

# 1
arr = np.arange(10, 20)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Ma:", np.max(arr))

# 2
arr = np.random.random(1000).astype(np.float64)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))

# 3
arr = np.random.randint(1, 100, (5, 5))

col2 = arr[:, 1]
row2 = arr[1, :]

flat = arr.flatten()

print("Array:", arr)
print("Column 2:", col2)
print("Row 2:", row2)
print("Flatten:", flat)

# 4
arr = np.random.random(500_000).astype(np.float64)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))