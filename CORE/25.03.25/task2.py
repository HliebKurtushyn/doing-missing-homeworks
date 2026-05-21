import os, sys
from datetime import datetime

path = input("шлях до директорії: ")

if not os.path.exists(path):
    print("директорії не існує")
    sys.exit()

while True:
    print("\nфайли в директорії:\n")

    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            mod_time = os.path.getmtime(full_path)

            print(f"""
                        Назва: {file}
                        Розмір: {size}
                        Дата зміни: {datetime.fromtimestamp(mod_time)}
                """)

    print("""
            1 - Перейменувати файл
            2 - Видалити файл
            3 - Створити теку
            4 - Вийти
        """)

    choice = input("Ваш вибір: ")

    if choice == "1":
        old_name = input("Старе ім'я файлу: ")
        new_name = input("Нове ім'я файлу: ")

        os.rename(
            os.path.join(path, old_name),
            os.path.join(path, new_name)
        )

        print("Файл перейменовано")

    elif choice == "2":
        file_name = input("Ім'я файлу для видалення: ")

        os.remove(os.path.join(path, file_name))

        print("Файл видалено")

    elif choice == "3":
        folder_name = input("Назва нової теки: ")

        os.mkdir(os.path.join(path, folder_name))

        print("Теку створено")

    elif choice == "4":
        print("Вихід...")
        break

    else:
        print("Невірний вибір")