students = {
    "Іванов": 5,
    "Петренко": 3,
    "Сидоренко": 4,
    "Коваль": 2,
    "Шевченко": 5
}

good_students = {}

for name, grade in students.items():
    if grade >= 4:
        good_students[name] = grade

print(good_students)