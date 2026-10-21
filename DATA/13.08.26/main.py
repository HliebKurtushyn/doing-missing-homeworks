import random
import time


# Завдання 1: Selection Sort з кінця
def selection_sort_end(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_idx = 0
        for j in range(1, i + 1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


print("Завдання 1:", selection_sort_end([64, 25, 12, 22, 11]))

# Завдання 2: Перевірка відносного порядку
data = [(5, 0), (2, 1), (5, 2), (1, 3)]
sorted_data = sorted(data, key=lambda x: x[0])
print("Завдання 2:", sorted_data)


# Завдання 3: Експеримент зі швидкістю
def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def selection_sort(arr):
    a = arr[:]
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < pivot]) + [x for x in arr if x == pivot] + quick_sort(
        [x for x in arr if x > pivot])


lst = [random.randint(1, 1000) for _ in range(100)]

t0 = time.time();
insertion_sort(lst);
t1 = time.time()
t2 = time.time();
selection_sort(lst);
t3 = time.time()
t4 = time.time();
quick_sort(lst);
t5 = time.time()
print(f"Завдання 3 -> Insertion: {t1 - t0:.6f}s | Selection: {t3 - t2:.6f}s | QuickSort: {t5 - t4:.6f}s")


# Завдання 4: Перевірка стабільності сортування вставками
def check_insertion_stability():
    arr = [(2, 0), (1, 1), (2, 2), (1, 3)]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    prev = {}
    for val, pos in arr:
        if val in prev and prev[val] > pos:
            return False
        prev[val] = pos
    return True


print("Завдання 4 (Стабільне?):", check_insertion_stability())


# Завдання 5: QuickSort з медіаною трьох
def quick_sort_median(arr):
    if len(arr) <= 1:
        return arr
    first, mid, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, mid, last])[1]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort_median(left) + middle + quick_sort_median(right)


print("Завдання 5:", quick_sort_median([3, 6, 8, 10, 1, 2, 1]))

# Завдання 6: Сортування CSV даних вибором проти вбудованого
csv_data = [("ProductC", 150), ("ProductA", 20), ("ProductB", 90)]

t0 = time.time()
sel_res = selection_sort(csv_data)  # адаптовано під кортежі за першим елементом або треба ключ
t1 = time.time()

t2 = time.time()
builtin_res = sorted(csv_data, key=lambda x: x[1])
t3 = time.time()
print(f"Завдання 6 -> Selection CSV: {t1 - t0:.6f}s | Built-in: {t3 - t2:.6f}s")


# Завдання 7: Консольна візуалізація процесу сортування
def visualize_sorting(arr):
    print("Завдання 7 (Візуалізація):")
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
        print(f"Крок {i + 1}: {a}")


visualize_sorting([7, 2, 1, 6, 8, 5])