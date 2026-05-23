import numpy as np

B = np.random.randint(1, 10, (2, 3, 4))
print("Оригінальний тривимірний масив B:\n", B)

# 6x4
B_reshaped = B.reshape(6, 4)
print("Масив після зміни форми:\n", B_reshaped)

# 1D
B_flattened = B_reshaped.flatten()
print("Одновимірний масив:\n", B_flattened)