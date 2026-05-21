import random

print("1 - кубик")
print("2 - випадкове число")
print("3 - переможець зі списку")

choice = input("> ")

if choice == "1":
    print(random.randint(1, 6))

elif choice == "2":
    a = int(input("від: "))
    b = int(input("до: "))
    print(random.randint(a, b))

elif choice == "3":
    items = input("введи через кому: ").split(",")
    print(random.choice([x.strip() for x in items]))

else:
    print("не треба вводити щось окрім 1, 2 або 3")