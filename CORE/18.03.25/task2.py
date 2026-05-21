class WeakPasswordError(Exception):
    pass


def check_password(password):
    try:
        if len(password) < 10:
            raise WeakPasswordError("занадто короткий")

        if not any(c.isupper() for c in password):
            raise WeakPasswordError("немає великих літер")

        if not any(c.isdigit() for c in password):
            raise WeakPasswordError("немає цифр")

        if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for c in password):
            raise WeakPasswordError("немає спецсимволів")

        print("пароль норм")

    except WeakPasswordError as e:
        print("слабкий пароль:", e)


check_password(input("Пароль: "))