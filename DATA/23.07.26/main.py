def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

print(count_vowels("hello world"))


def flatten_list(nested_list):
    return [item for sub in nested_list for item in sub]

print(flatten_list([[1, 2], [3, 4], [5, 6]]))


def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print(fibonacci(10))