total = 0

for i in range(1, 101):
    if i % 2 != 0:
        total += i

print("Сума непарних:", total)

print("-----------------------------")

text = input("Введи рядок: ")

first_letter = text[0]
count = text.count(first_letter)

print("Перша літера:", first_letter)
print("Кількість входжень:", count)