import random
import time

# Завдання 1: Час лінійного пошуку для початку, середини та кінця
lst = [random.randint(1, 100000) for _ in range(10000)]
target_start = lst[0]
target_mid = lst[5000]
target_end = lst[-1]

def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

t0 = time.perf_counter(); linear_search(lst, target_start); t1 = time.perf_counter()
t2 = time.perf_counter(); linear_search(lst, target_mid); t3 = time.perf_counter()
t4 = time.perf_counter(); linear_search(lst, target_end); t5 = time.perf_counter()

print(f"Завдання 1 -> Початок: {t1-t0:.8f}s | Середина: {t3-t2:.8f}s | Кінець: {t5-t4:.8f}s")