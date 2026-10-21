import copy
import math

# 1. Кортеж різних типів даних та словник їх типів
mixed_tuple = ("текст", 42, 3.14, [1, 2], True)
dict_types = {item: type(item).__name__ for item in mixed_tuple}
print("1:", dict_types)


# 2. Максимум і мінімум без вбудованих функцій
def min_max(tup):
    if not tup:
        return None, None
    mn = mx = tup[0]
    for x in tup[1:]:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx

print("2:", min_max((5, 2, 9, 1, 7)))


# 3. Другі елементи з трьох кортежів
def get_second_elements(tup_of_tuples):
    return tuple(t[1] for t in tup_of_tuples)

print("3:", get_second_elements(((1, 2, 3), (4, 5, 6), (7, 8, 9))))


# 4. Аналіз голосних та приголосних
def count_vowels_consonants(text):
    vowels = set("aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ")
    v_count = sum(1 for c in text if c in vowels)
    c_count = sum(1 for c in text if c.isalpha() and c not in vowels)
    return (v_count, c_count)

print("4:", count_vowels_consonants("Привіт світ"))


# 5. Середнє значення з округленням до двох знаків
def tuple_average(tup):
    if not tup:
        return 0.0
    return round(sum(tup) / len(tup), 2)

print("5:", tuple_average((10, 15, 20)))


# 6. Транспонування матриці (список кортежів)
def transpose_matrix(matrix):
    return [tuple(row[i] for row in matrix) for i in range(len(matrix[0]))]

print("6:", transpose_matrix([(1, 2, 3), (4, 5, 6)]))


# 7. Елементи першого кортежу, що є у другому
def filter_matching(tup1, tup2):
    s2 = set(tup2)
    return tuple(x for x in tup1 if x in s2)

print("7:", filter_matching((1, 2, 3, 4, 5), (3, 4, 5, 6, 7)))


# 8. Розділення та сортування рядків і чисел
def sort_strings_and_numbers(tup):
    strings = sorted([x for x in tup if isinstance(x, str)])
    numbers = sorted([x for x in tup if isinstance(x, (int, float))])
    return tuple(strings), tuple(numbers)

print("8:", sort_strings_and_numbers(("b", 5, "a", 1, "c", 3)))


# 9. Найменші елементи з необмеженої кількості кортежів
def min_elements(*tuples):
    return tuple(min(t) for t in tuples if t)

print("9:", min_elements((5, 8), (1, 9, 3), (10, 4)))


# 10. Тільки унікальні елементи (зустрічаються один раз)
def unique_elements(tup):
    counts = {x: tup.count(x) for x in tup}
    return tuple(x for x in tup if counts[x] == 1)

print("10:", unique_elements((1, 2, 2, 3, 4, 4, 5)))


# 11. Записи людей, вік яких перевищує середній
def above_average_age(records):
    if not records:
        return ()
    avg_age = sum(r[1] for r in records) / len(records)
    return tuple(r for r in records if r[1] > avg_age)

print("11:", above_average_age((("Олег", 20, "Dev"), ("Анна", 30, "QA"), ("Іван", 25, "PM"))))


# 12. Кортеж слова та його довжини
def word_lengths(text):
    return tuple((word, len(word)) for word in text.split())

print("12:", word_lengths("тест на довжину слів"))


# 13. Середня ціна для продуктів з однаковим ID (групування)
def average_product_prices(products):
    from collections import defaultdict
    data = defaultdict(list)
    for pid, price in products:
        data[pid].append(price)
    return tuple((pid, sum(prices) / len(prices)) for pid, prices in data.items())

print("13:", average_product_prices((("A", 10), ("B", 20), ("A", 30))))


# 14. Сортування за місяцем і днем народження
def sort_by_birthday(people):
    return sorted(people, key=lambda x: (x[1][5:], x[1][:4]))

print("14:", sort_by_birthday([("Оля", "2005-12-15"), ("Максим", "2002-01-10"), ("Іра", "2001-12-05")]))


# 15. Глибоке копіювання списку вкладених кортежів
def deep_copy_tuples(data):
    return copy.deepcopy(data)

print("15:", deep_copy_tuples([(1, (2, 3)), (4, (5, 6))]))


# 16. Фільтрація за простим віком і професією
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_people(people, letter):
    return [p for p in people if is_prime(p[1]) and p[2].lower().startswith(letter.lower())]

print("16:", filter_people([("Олексій", 7, "Developer"), ("Марія", 11, "Designer"), ("Петро", 13, "Driver")], "d"))


# 17. Система обробки фінансових транзакцій
def filter_by_type(transactions, t_type):
    return tuple(t for t in transactions if t[2] == t_type)

def filter_by_date(transactions, date):
    return tuple(t for t in transactions if t[3] == date)

txs = ((1, 100.0, "deposit", "2026-10-01"), (2, 50.0, "withdraw", "2026-10-02"), (3, 200.0, "deposit", "2026-10-01"))
print("17 (тип deposit):", filter_by_type(txs, "deposit"))
print("17 (дата 2026-10-01):", filter_by_date(txs, "2026-10-01"))


# 18. Матриця тригонометричних трансформацій
def transform_matrix(matrix, func):
    return tuple(tuple(func(val) for val in row) for row in matrix)

print("18:", transform_matrix(((0.0, math.pi/2), (math.pi, math.pi)), math.sin))