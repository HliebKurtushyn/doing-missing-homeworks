import numpy as np

# 1
array = np.array([12, -5, 7, 9, -3, 15])

result = np.append(array, 10)

print(result)

# 2
import numpy as np

arr = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])

result = np.delete(arr, 1, axis=0)

print(result)