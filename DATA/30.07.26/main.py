from collections import deque

# Завдання 1
queue = deque(["Антон", "Богдан", "Віка"])

print("Перший у черзі:", queue[0])
print("Обслуговуємо:", queue.popleft())
print("Тепер перший:", queue[0])


# Завдання 2
def is_valid_brackets(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

print(is_valid_brackets("({[()]})"))
print(is_valid_brackets("([)]"))
print(is_valid_brackets("{[}]"))