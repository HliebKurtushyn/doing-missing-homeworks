# 1

a = 5
b = 4

area = a * b

print(f"Площа прямокутника зі сторонами {a} та {b} дорівнює {area}.")

assert area == 20, "помилка"

# 3 (в завданнях там 2 пропущене чомусь)
year = int(input("Введіть рік: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} є високосним.")
else:
    print(f"{year} не є високосним.")

# 4
number = int(input("Введіть число для таблиці множення: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 5
number = 1
total = 0

while number <= 50:
    if number % 2 == 0:
        number += 1
        continue

    total += number
    number += 1

print(f"Сума непарних чисел від 1 до 50: {total}")

# 6
def create_full_name(first_name, last_name="Іванов"):
    return f"{last_name} {first_name}"


full_name1 = create_full_name(first_name="Петро", last_name="Петренко")
print(f"Повне ім'я: {full_name1}")

full_name2 = create_full_name(first_name="Олена")
print(f"Повне ім'я: {full_name2}")

assert full_name1 == "Петренко Петро", "Функція повинна повертати 'Петренко Петро'"
assert full_name2 == "Іванов Олена", "Функція повинна використовувати 'Іванов' як прізвище за замовчуванням"