colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}

name = input("Введи колір: ").lower()

if name in colors:
    print("RGB:", colors[name])
else:
    print("Колір не знайдено")