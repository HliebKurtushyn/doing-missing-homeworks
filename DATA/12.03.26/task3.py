import numpy as np

C = np.random.randint(1, 10, (3, 3, 3))
print("Оригінальний масив C:\n", C)

# сума по осі 0
sum_axis0 = np.sum(C, axis=0)
print("Сума по осі 0:\n", sum_axis0)

# сума по осі 1
sum_axis1 = np.sum(C, axis=1)
print("Сума по осі 1:\n", sum_axis1)

# загальна сума
total_sum = np.sum(C)
print("Загальна сума елементів масиву:", total_sum)