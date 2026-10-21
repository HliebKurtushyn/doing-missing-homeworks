import unittest
from collections import defaultdict

# --- Функції ---

def math_ops(a, b):
    div = a / b if b != 0 else None
    return a + b, a - b, a * b, div

def to_upper(s):
    return s.upper()

def is_palindrome(s):
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def multiply_by_seven(lst):
    return [x * 7 for x in lst]

def merge_dicts(d1, d2):
    res = defaultdict(int, d1)
    for k, v in d2.items():
        res[k] += v
    return dict(res)

def check_positive(n):
    if n < 0:
        raise ValueError("Число менше нуля")
    return n


# --- Юніт-тести ---

class TestHomework(unittest.TestCase):

    def test_math_ops(self):
        self.assertEqual(math_ops(10, 2), (12, 8, 20, 5.0))
        self.assertEqual(math_ops(-5, 5), (0, -10, -25, -1.0))

    def test_string_ops(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertFalse(is_palindrome("python"))

    def test_multiply_by_seven(self):
        self.assertEqual(multiply_by_seven([1, 2, 3]), [7, 14, 21])
        self.assertEqual(multiply_by_seven([]), [])
        self.assertEqual(multiply_by_seven([0]), [0])
        self.assertEqual(multiply_by_seven([-3, 5]), [-21, 35])

    def test_merge_dicts(self):
        self.assertEqual(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}), {"a": 1, "b": 5, "c": 4})
        self.assertEqual(merge_dicts({}, {"a": 5}), {"a": 5})
        self.assertEqual(merge_dicts({}, {}), {})

    def test_check_positive(self):
        self.assertEqual(check_positive(10), 10)
        self.assertEqual(check_positive(0), 0)
        with self.assertRaises(ValueError):
            check_positive(-1)

if __name__ == "__main__":
    unittest.main()