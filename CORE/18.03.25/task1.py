def load_config():
    try:
        with open("config.txt", "r") as f:
            data = f.read()
            print("Конфіг завантажено:\n", data)

    except FileNotFoundError:
        print("конфігу немає. створення дефолтного..")

        with open("config.txt", "w") as f:
            f.write("mode=default\nspeed=10\n")

        print("новий конфіг створено")

    finally:
        print("Операція з конфігом завершена")


load_config()