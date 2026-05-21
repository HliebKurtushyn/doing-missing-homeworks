import random

numbers = [random.randint(1, 50) for _ in range(10)]

print("Список чисел:", numbers)

if all(num > 10 for num in numbers):
    sorted_numbers = sorted(numbers)
    print("Усі числа більші за 10")
    print("Відсортований список:", sorted_numbers)
else:
    print("Не всі числа більші за 10")