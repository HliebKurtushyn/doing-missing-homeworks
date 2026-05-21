weather = {
    "Kyiv": 12,
    "Berlin": 18,
    "Paris": 15,
    "Rome": 20
}

cities = input("Введи міста через кому: ").split(",")

temps = []

for city in cities:
    city = city.strip()
    if city in weather:
        temps.append(weather[city])

if temps:
    print("Середня температура:", sum(temps) / len(temps))
else:
    print("Немає даних для цих міст")