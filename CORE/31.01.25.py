cube = lambda x: x ** 3
print("Куб 3:", cube(3))

is_multiple = lambda a, b: a % b == 0 if b != 0 else False
print("Кратність 10 і 5:", is_multiple(10, 5))
print("Кратність 10 і 3:", is_multiple(10, 3))

average = lambda a, b: (a + b) / 2
print("Середнє 4 і 6:", average(4, 6))

c_to_f = lambda c: c * 9/5 + 32
f_to_c = lambda f: (f - 32) * 5/9
print("25°C в Фаренгейтах:", c_to_f(25))
print("77°F в Цельсіях:", f_to_c(77))

hypotenuse = lambda a, b: (a**2 + b**2) ** 0.5
print("Гіпотенуза 3 і 4:", hypotenuse(3, 4))

is_leap = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("2024 високосний?", is_leap(2024))
print("1900 високосний?", is_leap(1900))

max_of_three = lambda a, b, c: max(a, b, c)
print("Максимум з 5, 12, 9:", max_of_three(5, 12, 9))