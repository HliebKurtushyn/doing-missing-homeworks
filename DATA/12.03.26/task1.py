import numpy as np

array1 = np.random.randint(-10, 11, (4, 4))
array2 = np.random.randint(-10, 11, (4, 4))
array3 = np.random.randint(-10, 11, (4, 4))

combined_array = np.stack((array1, array2, array3))

print("Об'єднаний масив з новою віссю:\n", combined_array)

assert combined_array.shape == (3, 4, 4), "Розмір об'єднаного масиву повинен бути (3, 4, 4)"