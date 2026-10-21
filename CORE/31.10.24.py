name = input("Ім'я: ")
weekday_mins = int(input("Хвилин у будній день: "))
weekend_mins = int(input("Хвилин у вихідний день: "))

weekdays_total = weekday_mins * 5
weekend_total = weekend_mins * 2
total_mins = weekdays_total + weekend_total
hours = total_mins / 60

print(f"\n{name} грає:")
print(f"{weekdays_total} хвилин у будні")
print(f"{weekend_total} хвилин у вихідні")
print(f"{total_mins} хвилин за тиждень")
print(f"Це {hours} години")