import re
import time


# Завдання 1: Пошук email-адрес
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return re.findall(pattern, text)


sample_text = "Звертайтесь сюди: test.user@gmail.com або support@domain.ua, а також fake-email@@com."
emails = extract_emails(sample_text)
print("Завдання 1:", emails)


# Завдання 2: Останній вхід за допомогою rfind() та rindex()
def find_last_occurrence(text, sub):
    return text.rfind(sub)


def index_last_occurrence(text, sub):
    try:
        return text.rindex(sub)
    except ValueError:
        return -1


text_ex = "hello world, welcome to python world!"
print("Завдання 2 (rfind):", find_last_occurrence(text_ex, "world"))
print("Завдання 2 (rindex відсутній):", index_last_occurrence(text_ex, "java"))


# Завдання 3: Алгоритм Бойера–Мура (поганий символ) та порівняння з find()
def bad_character_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0

    bad_char = bad_character_table(pattern)
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            return shift
        else:
            char = text[shift + j]
            if char in bad_char:
                shift += max(1, j - (m - 1 - bad_char[char]))
            else:
                shift += max(1, j)
    return -1


large_text = "AAB" * 10000 + "TargetPattern" + "AAB" * 10000
pattern = "TargetPattern"

t0 = time.perf_counter()
boyer_moore_search(large_text, pattern)
t1 = time.perf_counter()

t2 = time.perf_counter()
large_text.find(pattern)
t3 = time.perf_counter()

print(f"Завдання 3 -> Boyer-Moore: {t1 - t0:.6f}s | str.find(): {t3 - t2:.6f}s")