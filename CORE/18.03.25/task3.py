numbers = []

try:
    while True:
        user_input = input("Введи число або 'стоп': ")

        if user_input.lower() == "стоп":
            break

        numbers.append(int(user_input))

except ValueError:
    print("Це не число")

finally:
    print("Введені числа:", numbers)